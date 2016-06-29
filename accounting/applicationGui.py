import tkinter
import pickle


class AppGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter employee ID:')
        self.employee_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.employee_entry.pack(side='left')

        self.add_button = tkinter.Button(self.bottom_frame,text='Add', command=self.employee_add)
        self.edit_button = tkinter.Button(self.bottom_frame, text='Edit', command=self.employee_edit)
        self.payroll_button = tkinter.Button(self.bottom_frame, text='Payroll', command=self.employee_payroll)

        self.add_button.pack(side='left')
        self.edit_button.pack(side='left')
        self.payroll_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def employee_add(self):
        emp_id = float(self.employee_entry.get())

    def employee_edit(self):
        emp_id = float(self.employee_entry.get())

    def employee_payroll(self):
        open_file = open('hourly_employees', 'wb')
        hourly_data = {}
        pickle.dump(hourly_data, open_file)
        open_file.close()

        open_file = open('salaried_employees', 'wb')
        salaried_data = {}
        pickle.dump(salaried_data, open_file)
        open_file.close()

        open_file = open('receipts', 'wb')
        receipts_data = {}
        pickle.dump(receipts_data, open_file)
        open_file.close()

        open_file = open('timecards', 'wb')
        timecards_data = {}
        pickle.dump(timecards_data, open_file)
        open_file.close()


run_app = AppGUI()