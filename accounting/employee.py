class Employee:

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hourly_rate = hourly_rate
        self.__weekly_dues = weekly_dues

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def set_weekly_dues(self, weekly_dues):
        self.__weekly_dues = weekly_dues

    def get_full_name(self):
        return self.__last_name + ', ' + self.__first_name

    def get_hourly_rate(self):
        return self.__hourly_rate

    def get_weekly_dues(self):
        return self.__weekly_dues


