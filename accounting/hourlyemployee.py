from accounting.employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        Employee.__init__(first_name, last_name, weekly_dues)
        self.__hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self.__hourly_rate



