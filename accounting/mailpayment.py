from accounting.paymentmethod import PaymentMethod


class MailPayment(PaymentMethod):

    def __init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission ):
        PaymentMethod.__init__(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission)

    def pay(self, first_name, last_name, street_address, city, state, zip_code, total_pay, commission):
        total = total_pay + commission
        return 'Mailing check to' + first_name + ' ' + last_name + ' ' + 'for $' + total + ' ' + street_address + ' ' + city + ', ' + state + ' ' + zip_code
    