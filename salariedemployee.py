from accounting.employee import Employee
from accounting.receipt import Receipt


class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, weekly_dues, sale_date, sale_amt, salary, commission_rate, pay):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        Receipt.__init__(sale_date, sale_amt)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__pay = pay
        self.__receipts = []

    def make_sale(self, amt):
        sale_amt = Receipt(self, amt)
        self.__receipts.append(sale_amt)

    def get_date(self, date):
        return self.__date

    def get_pay(self, start_date, end_date, date, commission_rate):
        total_pay = 0
        for amt in self.__receipts:
            if date >= start_date and date <= end_date:
                pay = Receipt.calculate_commission()
                pay += total_pay
        return pay

    def pay(self, pay):
        return self.__pay

