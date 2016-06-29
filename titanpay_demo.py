
import employee
import salariedemployee
import address
import timecard
import receipt
import bankaccount

EMPLOYEE = 1
SALARIED_EMP = 2
QUIT = 3
HOURS = 8
OVERTIME = 1.5
SALARY_HOURS = 160
YEAR_SALARY_HOURS = 2080
COMMISSION_CONVERT = 100


def main():

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == 1:
            get_hourly_employee()
        elif choice == 2:
            get_salary_employee()
        elif choice == 3:
            print('Thank you for using the Titan Pay Time System')


def get_menu_choice():
    print()
    print('Welcome to the employee pay module!')
    print('Is the employee "hourly" or "salaried"? ')
    print('Hourly: Enter 1.')
    print('Salary: Enter 2.')
    print('Quit: Enter 3.')

    choice = int(input('Enter choice: '))

    while choice < EMPLOYEE or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    return choice


def get_hourly_employee():
    emp_id = input('Enter the employee ID: ')
    first = input('Enter first name of the employee: ')
    last = input('Enter last name of the employee: ')
    rate = float(input('Enter the employees hourly rate: '))
    dues = float(input('Enter the employees weekly dues: '))
    employee_data = employee.Employee(emp_id, first, last, rate, dues)
    print()

    print('Enter the employees address.')
    street = input('Street Address: ')
    city = input('City: ')
    state = input('State: ')
    zipcode = input('Zip: ')
    address_data = address.Address(street, city, state, zipcode)
    print()

    print('Please enter your time worked today.')
    date = input('Enter today\'s date (MM/DD/YY): ')
    start = float(input('Enter start time (AM): '))
    end = float(input('Enter end time (PM): '))
    time_data = timecard.TimeCard(date, start, end)
    hours = time_data.calculate_daily_pay()                           # setup for loop to calc 7 days week totals
    if hours > HOURS:
        overtime_pay = ((hours - HOURS) * OVERTIME * employee_data.get_hourly_rate())
        regular_pay = (HOURS * employee_data.get_hourly_rate())
        total_pay = overtime_pay + regular_pay
    else:
        total_pay = (HOURS * employee_data.get_hourly_rate())

    deposit = total_pay - employee_data.get_weekly_dues()
    print()

    print('Enter your bank account information.')
    bank = input('Enter your bank name: ')
    routing = input('Enter the routing number: ')
    account = input('Enter the account number: ')
    bank_data = bankaccount.BankAccount(bank, routing, account)
    print()

    print(str(employee_data.get_full_name()))
    print(str(address_data.get_address()))
    print('Depositing $', format(deposit, ',.2f'), 'in', str(bank_data.get_bank_name()), 'Account Number:', \
          str(bank_data.get_account_id()), 'using Routing Number:', \
          str(bank_data.get_routing_number()), sep=' ')
    print()


def get_salary_employee():
    emp_id = input('Enter the employee ID: ')
    first = input('Enter first name of the employee: ')
    last = input('Enter last name of the employee: ')
    salary = float(input('Enter the employees salary: '))
    commission = float(input('Enter the employees commission rate(%): '))
    dues = float(input('Enter the employees weekly dues: '))
    employee_data = salariedemployee.SalariedEmployee(emp_id, first, last, salary, commission, dues)

    print('Enter the employees address.')
    street = input('Street Address: ')
    city = input('City: ')
    state = input('State: ')
    zipcode = input('Zip: ')
    address_data = address.Address(street, city, state, zipcode)
    print()

    print('Enter the employee\'s sales data.')
    date = input('Enter today\'s date (MM/DD/YY): ')
    sales = float(input('Please enter the employee\'s sales: '))
    receipt_data = receipt.Receipt(date, sales)                 # setup for loop to calc sales receipts over month
    print()

    salary_pay = (salary / YEAR_SALARY_HOURS) * SALARY_HOURS  # needs to be updated to account for 5 week months
    commission_pay = receipt_data.get_sales() * commission / COMMISSION_CONVERT
    deposit = salary_pay + commission_pay - employee_data.get_weekly_dues()

    print('Enter your bank account information.')
    bank = input('Enter your bank name: ')
    routing = input('Enter the routing number: ')
    account = input('Enter the account number: ')
    bank_data = bankaccount.BankAccount(bank, routing, account)
    print()

    print(str(employee_data.get_full_name()))
    print(str(address_data.get_address()))
    print('Depositing your monthly paycheck...')
    print('Depositing $', format(deposit, ',.2f'), 'in', str(bank_data.get_bank_name()), 'Account Number:', \
          str(bank_data.get_account_id()), 'using Routing Number:', \
          str(bank_data.get_routing_number()), sep=' ')
    print()

main()