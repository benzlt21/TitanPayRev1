from accounting.paymentmethod import PaymentMethod


class Employee:

    def __init__(self, employee_id, first_name, last_name, weekly_dues, payment_method):
        PaymentMethod.__init__(payment_method)
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues

    def get_full_name(self):
        return self.__last_name + ', ' + self.__first_name

    def get_weekly_dues(self):
        return self.__weekly_dues