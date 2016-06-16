from accounting.paymentmethod import PaymentMethod
from accounting.bankaccount import BankAccount


class DirectDepositPayment(PaymentMethod):

    def __init__(self, payment_method, total_pay, commission, bank_name, routing_number, account_id):
        PaymentMethod.__init__(payment_method, total_pay, commission)
        BankAccount.__init__(bank_name, routing_number, account_id)

    def pay(self, total_pay, commission, bank_name, routing_number, account_id):
        total = total_pay + commission
        return 'Depositing $', format(total, ',.2f'), 'in', bank_name, 'Account Number:', account_id, \
               'using Routing Number: ', routing_number