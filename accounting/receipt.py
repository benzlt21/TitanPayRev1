class Receipt:

    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = sale_amt

    def set_date(self, date):
        self.__date = date

    def set_sale_amt(self, sale_amt):
        self.__sale_amt = sale_amt

    def get_sales(self):
        return self.__sale_amt


