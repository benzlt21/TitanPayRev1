from accounting.employee import Employee
from accounting.timecard import TimeCard

HOURS = 8
OVERTIME = 1.5


class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, weekly_dues, start_date, end_date, start_time, end_time, rate, pay):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        TimeCard.__init__(start_date, end_date, start_time, end_time)
        self.__rate = rate
        self.__pay = pay
        self.__time_card = []

    def get_hourly_rate(self, rate):
        return self.__rate

    def get_date(self, date):
        return self.__date

    def clock_in(self, start_date, start_time):
        startTime = TimeCard(self, start_date, start_time)
        self.__time_card.append(startTime)

    def clock_out(self, end_date, end_time, date):
        endTime = TimeCard(self, end_date, end_time)
        for date in self.__time_card:
                self.__time_card.append(endTime)

    def get_pay(self, start_date, end_date, date):
        total_pay = 0
        for date in self.__time_card:
            if date >= start_date and date <= end_date:
                pay = TimeCard.calculate_daily_pay()
                pay += total_pay

        return pay

    def pay(self, pay):
        return self.__pay
