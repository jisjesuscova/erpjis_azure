from app.models.models import BankModel

class Bank():
    @staticmethod
    def get():
        banks = BankModel.query.order_by(BankModel.bank).all()

        return banks