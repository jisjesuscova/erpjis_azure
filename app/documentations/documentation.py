from flask import request
from app.models.models import DocumentationModel, DocumentationSubTitleModel, DocumentationTitleModel
from app import db
from datetime import datetime
import markdown
from app.helpers.helper import Helper
from bs4 import BeautifulSoup
import unicodedata

class Documentation():
    @staticmethod
    def get(id = '', page = 1):
        if id != '':
            documentation = DocumentationModel.query.filter_by(id=id).first()

            return documentation
        else:
            documentations = DocumentationModel.query.order_by(DocumentationModel.added_date.desc()).paginate(page=page, per_page=20, error_out=False)

            return documentations
        
    
    def get_last_row():
        documentation = DocumentationModel.query.order_by(DocumentationModel.added_date.desc()).first()

        return documentation.id

    @staticmethod
    def store(data):
        title = Helper.get_documentation_main_title(data['description'])
        title = Helper.fix_documentation_titles(str(title))
        title = Helper.clean_string(str(title))

        documentation = DocumentationModel()
        documentation.title = title
        documentation.original_description = data['description']
        documentation.markdown_description = markdown.markdown(data['description'])
        documentation.added_date = datetime.now()
        documentation.updated_date = datetime.now()

        db.session.add(documentation)

        try:
            db.session.commit()

            id = Documentation.get_last_row()

            Documentation.store_titles(id, data['description'])

            Documentation.update_tags(id, data['description'])

            return 1
        except Exception as e:
            return 0
        
    @staticmethod
    def store_titles(id, description):
        html_text = markdown.markdown(description)
        soup = BeautifulSoup(html_text, 'html.parser')
        h1_tags = soup.find_all('h1')
        h2_tags = soup.find_all('h2')

        for h1 in h1_tags:
            title = h1.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()
            
        for h2 in h2_tags:
            title = h2.string
            title = Helper.fix_documentation_titles(str(title))
            tag = Helper.clean_string(str(title))
            documentation_sub_title = DocumentationSubTitleModel()
            documentation_sub_title.documentation_id = id
            documentation_sub_title.documentation_title_id = documentation_title.id
            documentation_sub_title.title = title
            documentation_sub_title.tag = tag
            documentation_sub_title.added_date = datetime.now()
            documentation_sub_title.updated_date = datetime.now()
            db.session.add(documentation_sub_title)
            db.session.commit()

        return 1
    
    @staticmethod
    def update_tags(id, description):
        html_text = markdown.markdown(description)
        soup = BeautifulSoup(html_text, "html.parser")
        for h2 in soup.find_all("h2"):
            h2["id"] = unicodedata.normalize('NFKD', h2.string).encode('ASCII', 'ignore').decode('utf-8')
            h2["id"] = h2["id"].lower().replace(".", "")
            h2["id"] = h2["id"].lower().replace(" ", "-")

        documentation = DocumentationModel.query.filter_by(id = id).first()
        documentation.description = soup
        db.session.add(documentation)
        db.session.commit()

        return 1

       