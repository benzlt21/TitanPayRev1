HOURS = 8
OVERTIME = 1.5


class TimeCard:

    def __init__(self, date, start_time, end_time, rate):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.rate = rate

    def calculate_daily_pay(self, start_time, end_time, rate):
        hours = (end_time + 12) - start_time
        if hours <= HOURS:
            total_pay = (HOURS * rate)
        else:
            overtime_pay = ((hours - HOURS) * OVERTIME * rate)
            regular_pay = (HOURS * rate)
            total_pay = overtime_pay + regular_pay
        return total_pay



