class Receipt:

    def __init__(self, sale_date, sale_amt):
        self.__sale_date = sale_date
        self.__sale_amt = sale_amt

    def get_sales(self):
        return self.__sale_amt


