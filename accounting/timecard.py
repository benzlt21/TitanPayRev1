STANDARD = 8
OVERTIME = 1.5


class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def set_date(self, date):
        self.__date = date

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def set_end_time(self, end_time):
        self.__end_time = end_time

    def calculate_daily_pay(self):

        return (self.__end_time + 12) - self.__start_time


