from app.models.models import WhatsappTemplateModel

class WhatsappTemplate():
    @staticmethod
    def get(id):
        whatsapp_template = WhatsappTemplateModel.query.filter_by(id=id).first()

        return whatsapp_template