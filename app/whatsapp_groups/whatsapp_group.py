from app.models.models import WhatsappGroupModel

class WhatsappGroup():
    @staticmethod
    def get(id = ''):
        if id == '':
            whatsapp_groups = WhatsappGroupModel.query.order_by('whatsapp_group').all()

            return whatsapp_groups
        else:
            whatsapp_groups = WhatsappGroupModel.query.filter_by(id=id).first()

            return whatsapp_groups
