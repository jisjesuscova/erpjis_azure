from flask import request
from app.models.models import DocumentationModel, PreDocumentationModel, DocumentationTitleModel
from app import db
from datetime import datetime
import markdown
from app.helpers.helper import Helper
from bs4 import BeautifulSoup

class Documentation():
    @staticmethod
    def get(page):
        documentations = DocumentationModel.query.order_by(DocumentationModel.added_date.desc()).paginate(page=page, per_page=20, error_out=False)

        return documentations
    
    def get_last_row():
        documentation = DocumentationModel.query.order_by(DocumentationModel.added_date.desc()).first()

        return documentation.id

    @staticmethod
    def store(data):
        title = Helper.get_documentation_main_title(data['description'])
        title = Helper.fix_documentation_titles(str(title))

        documentation = DocumentationModel()
        documentation.title = title
        documentation.description = markdown.markdown(data['description'])
        documentation.added_date = datetime.now()
        documentation.updated_date = datetime.now()

        db.session.add(documentation)

        try:
            db.session.commit()

            id = Documentation.get_last_row()

            Documentation.store_titles(id, data['description'])

            return 1
        except Exception as e:
            return 0
        
    @staticmethod
    def store_titles(id, description):
        html_text = markdown.markdown(description)
        soup = BeautifulSoup(html_text, 'html.parser')
        h1_tags = soup.find_all('h1')
        h2_tags = soup.find_all('h2')
        h3_tags = soup.find_all('h3')
        h4_tags = soup.find_all('h4')
        h5_tags = soup.find_all('h5')
        h6_tags = soup.find_all('h6')

        for h1 in h1_tags:
            title = h1.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.level_id = 1
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()
            
        for h2 in h2_tags:
            title = h2.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.level_id = 2
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()
            
        for h3 in h3_tags:
            title = h3.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.level_id = 3
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()

        for h4 in h4_tags:
            title = h4.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.level_id = 4
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()

        for h5 in h5_tags:
            title = h4.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.level_id = 5
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()

        for h6 in h6_tags:
            title = h4.string
            title = Helper.fix_documentation_titles(str(title))
            documentation_title = DocumentationTitleModel()
            documentation_title.documentation_id = id
            documentation_title.level_id = 6
            documentation_title.title = title
            documentation_title.added_date = datetime.now()
            documentation_title.updated_date = datetime.now()
            db.session.add(documentation_title)
            db.session.commit()

        return 1

       