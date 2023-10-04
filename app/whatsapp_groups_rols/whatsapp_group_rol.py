from app.models.models import WhatsappGroupRolModel

class WhatsappGroupRol():
    @staticmethod
    def get(group_id = ''):
        whatsapp_groups_rols = WhatsappGroupRolModel.query.filter_by(group_id=group_id).all()

        return whatsapp_groups_rols