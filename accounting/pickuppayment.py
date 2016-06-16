from accounting.paymentmethod import PaymentMethod
from accounting.employee import Employee


class PickUpPayment(PaymentMethod):

    def __init__(self, payment_method, total_pay, commission, employee_id, first_name, last_name, weekly_dues):
        PaymentMethod.__init__(payment_method, total_pay, commission)
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)

    def pay(self, first_name, last_name, total_pay, commission):
        total = total_pay + commission
        return 'A check for $', total, ' is waiting for ', first_name, ' ', last_name, ' at the PostMaster.'