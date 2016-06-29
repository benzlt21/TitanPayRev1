from accounting.paymentmethod import PaymentMethod
from accounting.employee import Employee
from accounting.address import Address


class MailPayment(PaymentMethod):

    def __init__(self, payment_method, total_pay, commission, first_name, last_name, street_address, city, state, zip_code):
        PaymentMethod.__init__(payment_method, total_pay, commission)
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        Address.__init__(street_address, city, state, zip_code)

    def pay(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission):
        total = total_pay + commission
        return 'Mailing check to' + first_name + ' ' + last_name + ' ' + 'for $' + total + ' ' + street_address + ' ' \
               + city + ', ' + state + ' ' + zip_code
