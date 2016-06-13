from accounting.paymentmethod import PaymentMethod


class PickUpPayment(PaymentMethod):

    def __init__(self, first_name, last_name, total_pay, commission ):
        PaymentMethod.__init__(self, first_name, last_name, total_pay, commission)

    def pay(self, first_name, last_name, total_pay, commission):
        total = total_pay + commission
        return 'A check for $' + total + ' is waiting for ' + first_name + ' ' + last_name + ' at the PostMaster.'