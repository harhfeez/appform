from tkinter import *
class App_Form(Frame):
    def __init__(self, master):
        super(App_Form, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = Label(self, text="APPLICATION FORM")
        self.lbl_title.grid(row=0, column=0, columnspan=2, sticky=E)
        self.lbl_empty = Label(self, text="").grid(row=1, column=0)

        self.lbl_fullname = Label(self, text= "Full Name: ")
        self.lbl_fullname.grid(row=3, column=0, sticky=W)
        self.txt_fullname = Entry(self, width=10)
        self.txt_fullname.grid(row=3, column=1, columnspan=2, sticky=W)

        self.txt_fullname = Entry(self, width=15)
        self.txt_fullname.grid(row=3, column=2, columnspan=2, sticky=W)
        self.lbl_empty = Label(self, text="").grid(row=3, column=3)

        self.lbl_empty = Label(self, text="").grid(row=4, column=0)

        self.lbl_age = Label(self, text= "Age: ")
        self.lbl_age.grid(row=5, column=0, sticky=W)
        self.txt_age = Entry(self, width=7)
        self.txt_age.insert(0,"ex: 23")
        self.txt_age.grid(row=5, column=1, columnspan=2, sticky=W)

        self.lbl_empty = Label(self, text="").grid(row=6, column=0)

        self.lbl_email = Label(self, text= "E-mail: ")
        self.lbl_email.grid(row=7, column=0, sticky=W)
        self.txt_email = Entry(self, width=30)
        self.txt_email.grid(row=7, column=1, columnspan=2, sticky=W)
        self.txt_email.insert(0,"ex: myname@example.com")
       # self.txt_email.setvar(self.txt_email.insert(1))

        self.lbl_empty = Label(self, text="").grid(row=8, column=0)

        self.gender = StringVar()
        self.lbl_gender = Label(self, text="Gender: ")
        self.lbl_gender.grid(row=9, column=0, sticky=W)
        self.rad_male = Radiobutton(self, text="Male", value="Male", variable=self.gender)
        self.rad_male.grid(row=9, column=1, sticky=W)
        self.rad_female = Radiobutton(self, text="Female", value="Female", variable=self.gender)
        self.rad_female.grid(row=9, column=2, sticky=W)
        self.rad_male.select()

        self.lbl_empty = Label(self, text="").grid(row=10, column=0)

        self.marital_status = StringVar()
        self.marital_status_values = ['single', 'Married','Divorced', 'Single N Searching', 'Complicated']
        self.lbl_marital_status = Label(self, text="Marital status: ")
        self.lbl_marital_status.grid(row=11, column=0, sticky=W)
        self.option_marital_status = OptionMenu(self, self.marital_status, *self.marital_status_values)
        self.option_marital_status.grid(row=11, column=1, columnspan=2, sticky=W)
        self.marital_status.set(self.marital_status_values[0])

        line = 12
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.lbl_address = Label(self, text= "Address: ")
        self.lbl_address.grid(row=line, column=0, sticky=W)
        self.txt_address = Text(self, width=33, height=2)
        self.txt_address.grid(row=line, column=1, columnspan=2, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)


        line += 1
        self.lbl_phone_num = Label(self, text= "Phone Number: ")
        self.lbl_phone_num.grid(row=line, column=0, sticky=W)
        self.txt_phone_num = Entry(self, width=13)
        self.txt_phone_num.grid(row=line, column=1, columnspan=2, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.lbl_we = Label(self, text="Working Experience: ")
        self.lbl_we.grid(row=line, column=0, sticky=W)
        self.txt_we = Text(self, width=25, height=5)
        self.txt_we.grid(row=line, column=1, columnspan=2, sticky=W)
        self.yscrollbar = Scrollbar(self, command=self.txt_we.yview)
        self.yscrollbar.grid(row=line, column=3, sticky='nsew')
        self.txt_we['yscrollcommand'] = self.yscrollbar.set

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.btn_reset = Button(self, text="Reset", width=10, command=self.reset)
        self.btn_reset.grid(row=line, column=0, sticky=E)
        self.btn_submit = Button(self, text="Submit", width=10,command=self.submit)
        self.btn_submit.grid(row=line, column=1, sticky=W)

    def reset(self):
        self.txt_fullname.delete(0, END)
        self.txt_age.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_address.delete(0.0, END)
        self.txt_phone_num.delete(0, END)
        self.rad_male.select()
        self.marital_status.set(self.marital_status_values[0])
        self.txt_we.delete(0.0, END)


    def submit(self):
        data = '\nFull Name: ' +self.txt_fullname.get()
        data += '\nAge: ' +self.txt_age.get()
        data += '\nE-mail: ' +self.txt_email.get()
        data += '\nAddress: ' +self.txt_address.get(1.0, END)
        data +='\nPhone Number: '+self.txt_phone_num.get()
        data += '\nGender: ' +self.gender.get()
        data += '\nMarital status: ' +self.marital_status.get()
        data += '\nWorking Experience: ' + self.txt_we.get(1.0, END)
        data +='\n\n'
        print(data)
        with open('Application form.txt', 'a') as f:
            f.write(data)
            f.close()
        self.reset()
window = Tk()
window.title("APPLICATION FORM")
window.geometry('400x500')
app = App_Form(window)
app.mainloop()