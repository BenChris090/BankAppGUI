#User Interface Calculator
from tkinter import *
from tkinter import messagebox
import json
from utils.user_db_handler import * # asteric sign(*) imports all

def home():
    def clear():
        userentry.delete("0", "end")
        passentry.delete("0", "end")

    def close():
        window.destroy()

    def login1():
        if email.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Enter Email And Password", parent = window)
        else:
            try:
                email1 = email.get()
                passw = password.get()

                result = login(email1, passw)
                if result:
                    messagebox.showinfo("Success", "Login success", parent = window)
                    window.destroy()
                    Bank()
                else:
                    messagebox.showerror("Error", "Login failure :  Invalid Email Or Password", parent = window)
            except Exception as  es:
                messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = window)


    window = Tk()#instantiation
    window.title("Login Portal")
    window.maxsize(width = 500,  height = 500)
    window.minsize(width = 500,  height = 500)

    heading = Label(window, text = "Login", font = "Candara 25 bold")
    heading.place(x = 80, y = 150)

    email = Label(window, text = "Email :", font = "Candara 10 bold")
    email.place(x = 80, y = 220)

    userpass = Label(window, text = "Password :", font = "Candara 10 bold")
    userpass.place(x = 80, y = 260)

    email = StringVar()
    password = StringVar()

    userentry = Entry(window, width = 40, textvariable = email)
    userentry.focus()
    userentry.place(x = 200, y = 223)

    passentry = Entry(window, width = 40, show = "*", textvariable = password)
    passentry.place(x = 200, y = 260)

    btn_login = Button(window, text = "Login", font = "Candara 10 bold", command = login1) #command missing
    btn_login.place(x = 200, y = 293)

    btn_login = Button(window, text = "Clear", font = "Candara 10 bold", command = clear) #command missing
    btn_login.place(x = 260, y = 293)

    sign_up_btn = Button(window, text = "Switch To Sign Up", command = signup) #command missing
    sign_up_btn.place(x = 350, y = 20)

    window.mainloop()


def Bank():
    users = read_user()
    user = [user for user in  users if user["is active"] == "True"]
    email1 = user[0]["email"]
    passw = user[0]["password"]
    
    def log_out():
        logout(email1)
        bank.destroy()
        home()

    def account_info():
        bank.destroy()
        user = read_user(email1)

        def goBack():
            ac_ver.destroy()



        def acc_info():

            def go_back():
                info.destroy()
                Bank()


            if verPin.get() != "" and verPin.get() == user["transact_pin"]:
                
                ac_ver.destroy()

                info = Tk()
                info.title("Ice_Berg Mobile")
                info.maxsize(width = 500, height = 500)
                info.minsize(width = 500, height = 500)

                heading = Label(info, text = "Welcome To Ice_Berg Mobile", font = "Candara 25 bold")
                heading.place(x = 40, y = 150)

                label1 = Label(info, text = "Account Name : {0}".format(user["account_name"]), font = "Candara 15 bold")
                label1.place(x = 120, y = 223)

                label2 = Label(info, text = "Mobile Number : {0}".format(user["mobile_number"]), font = "Candara 15 bold")
                label2.place(x = 120, y = 263)

                label3 = Label(info, text = "Email : {0}".format(user["email"]), font = "Candara 15 bold")
                label3.place(x = 120, y = 303)

                label4 = Label(info, text = "Account Number : {0}".format(user["account_number"]), font = "Candara 15 bold")
                label4.place(x = 120, y = 343)

                label5 = Label(info, text = "Account Balance : N {0}".format(user["account_balance"]), font = "Candara 15 bold")
                label5.place(x = 120, y = 383)
                
                back = Button(info, text = "<-- Back", command = go_back) #command is missing
                back.place(x = 350, y = 20)


                info.mainloop()
            else:
                messagebox.showerror("Error", "Invalid Pin", parent = ac_ver)

        
        ac_ver = Tk()
        ac_ver.title("Ice_Berg Mobile")
        ac_ver.maxsize(width = 500, height = 500)
        ac_ver.minsize(width = 500, height = 500)

        heading = Label(ac_ver, text = "Welcome To Ice_Berg Mobile", font = "Candara 25 bold")
        heading.place(x = 40, y = 150)

        label1 = Label(ac_ver, text = "Enter Your Pin Below", font = "Candara 15 bold")
        label1.place(x = 150, y = 223)

        entry = StringVar()

        verPin = Entry(ac_ver, width = 34, show = "*", textvariable = entry)
        verPin.place(x = 150, y = 263)

        click = Button(ac_ver, text = "Show Account Info", font = "Candara 10 bold", padx=45, command = acc_info)# awaiting action
        click.place(x = 150, y = 303)

        back = Button(ac_ver, text = "<-- Back", command = goBack) #command is missing
        back.place(x = 350, y = 20)

        ac_ver.mainloop()

    
    def depositFunds():
        bank.destroy()
        user = read_user(email1)

        def switchBack():
            deposit.destroy()

        def clean():
            amnt.delete('0', 'end')
            depoPin.delete('0', 'end')

        def confirmDeposit():
            if amnt.get() == "" or depoPin.get() == "":
                messagebox.showerror("Error", "All Fields Are Required",  parent = deposit)
            elif depoPin.get().isdigit == False or depoPin.get() != user["transact_pin"]:
                messagebox.showerror("Error", "Invalid Pin", parent = deposit)
            elif amnt.get().isdigit() == False or int(amnt.get()) < 500:
                messagebox.showerror("Error", "Invalid Amount", parent = deposit) 
            else:
                try:
                    amount = int(amnt.get())
                    pin = depoPin.get()

                    result = depositNow(email1, amount, pin)
                    if result:
                        messagebox.showinfo("Success", "{0} Deposited Successful".format(amount), parent = deposit)
                        clean()
                        switchBack()
                    else:
                        messagebox.showerror("Error", "Pin Is Invalid", parent = deposit)
                except Exception as  es:
                    messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = deposit)





        deposit = Tk()
        deposit.title("Ice_Berg Mobile")
        deposit.maxsize(width = 500, height = 500)
        deposit.minsize(width = 500, height = 500)

        heading = Label(deposit, text = "Welcome To Ice_Berg Mobile", font = "Candara 25 bold")
        heading.place(x = 40, y = 150)

        label01 = Label(deposit, text = "Enter Amount :", font = "Candara 10 bold")
        label01.place(x = 80, y = 220)

        label02 = Label(deposit, text = "Enter Your Pin :", font = "Candara 10 bold")
        label02.place(x = 80, y = 260)

        amnt1 = StringVar()
        depoPin1 = StringVar()

        amnt = Entry(deposit, width = 40, textvariable = amnt1)
        amnt.place(x = 200, y = 223)

        depoPin = Entry(deposit, width = 40 , show = "*", textvariable = depoPin1)
        depoPin.place(x = 200, y = 260)

        btn_confirm = Button(deposit, text = "Confirm Deposit", font = "Candara 10 bold", command = confirmDeposit) #command is missing
        btn_confirm.place(x = 200, y = 297)

        btn_clear = Button(deposit, text = "Clear", font = "Candara 10 bold", command = clean) #command is missing
        btn_clear.place(x = 300, y = 297)

        switchLogin = Button(deposit, text = "<-- Back", command = switchBack) #command is missing
        switchLogin.place(x = 350, y = 20)

        deposit.mainloop()


    def withdrawFunds():
        bank.destroy()
        user = read_user(email1)

        def returnBack():
            withdraw.destroy()

        def cleanUp():
            amnt2.delete('0', 'end')
            withdrawPin.delete('0', 'end')

        def confirmWithdrawal():
            if amnt2.get() == "" or withdrawPin.get() == "":
                messagebox.showerror("Error", "All Fields Are Required",  parent = withdraw)
            elif withdrawPin.get().isdigit == False or withdrawPin.get() != user["transact_pin"]:
                messagebox.showerror("Error", "Invalid Pin", parent = withdraw)
            elif amnt2.get().isdigit() == False or int(amnt2.get()) < 500:
                messagebox.showerror("Error", "Invalid Amount", parent = withdraw)
            elif user["account_balance"] - int(amnt2.get()) < 0:
                messagebox.showerror("Error", "Insufficient Funds", parent = withdraw)
            else:
                try:
                    amount = int(amnt2.get())
                    pin = withdrawPin.get()

                    result = withdrawNow(email1, amount, pin)
                    if result:
                        messagebox.showinfo("Success", "{0} Withdrawn Successful".format(amount), parent = withdraw)
                        cleanUp()
                        returnBack()
                    else:
                        messagebox.showerror("Error", "Pin Is Invalid", parent = withdraw)
                except Exception as  es:
                    messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = withdraw)

        withdraw = Tk()
        withdraw.title("Ice_Berg Mobile")
        withdraw.maxsize(width = 500, height = 500)
        withdraw.minsize(width = 500, height = 500)

        heading = Label(withdraw, text = "Welcome To Ice_Berg Mobile", font = "Candara 25 bold")
        heading.place(x = 40, y = 150)

        label001 = Label(withdraw, text = "Enter Amount :", font = "Candara 10 bold")
        label001.place(x = 80, y = 220)

        label002 = Label(withdraw, text = "Enter Your Pin :", font = "Candara 10 bold")
        label002.place(x = 80, y = 260)

        amnt3 = StringVar()
        depoPin3 = StringVar()

        amnt2 = Entry(withdraw, width = 40, textvariable = amnt3)
        amnt2.place(x = 200, y = 223)

        withdrawPin = Entry(withdraw, width = 40 , show = "*", textvariable = depoPin3)
        withdrawPin.place(x = 200, y = 260)

        btn_cnfrm = Button(withdraw, text = "Confirm Withdrawal", font = "Candara 10 bold", command = confirmWithdrawal) #command is missing
        btn_cnfrm.place(x = 170, y = 297)

        btn_clear = Button(withdraw, text = "Clear", font = "Candara 10 bold", command = cleanUp) #command is missing
        btn_clear.place(x = 300, y = 297)

        rtrnBck = Button(withdraw, text = "<-- Back", command = returnBack) #command is missing
        rtrnBck.place(x = 360, y = 20)

        withdraw.mainloop()


    def transferFunds():
        bank.destroy()
        user = read_user(email1)

        def leanBack():
            transfer.destroy()
            Bank()

        def clearUp():
            beneficiary.delete('0', 'end')
            amntToTransfer.delete('0', 'end')
            transfPin.delete('0', 'end')

        def confirmTransfer():
            beneficiary1 = read_beneficiary(int(beneficiary.get()))
            if beneficiary.get() == "" or amntToTransfer.get() == "" or transfPin.get() == "":
                messagebox.showerror("Error", "All Fields Are Required",  parent = transfer)
            elif transfPin.get().isdigit() == False or transfPin.get() != user["transact_pin"]:
                messagebox.showerror("Error", "Invalid Pin", parent = transfer)
            elif amntToTransfer.get().isdigit() == False or int(amntToTransfer.get()) < 500:
                messagebox.showerror("Error", "Invalid Amount", parent = transfer)
            elif user["account_balance"] - int(amntToTransfer.get()) < 0:
                messagebox.showerror("Error", "Insufficient Funds", parent = transfer)
            else:
                try:
                    accountNo = int(beneficiary.get())
                    amount1 = int(amntToTransfer.get())
                    pin1 = transfPin.get()

                    result = transferNow(email1, accountNo, amount1, pin1)
                    if result:
                        messagebox.showinfo("Success", "N{0} Transfered To {1} Successfully".format(amount1, beneficiary1["account_name"]), parent = transfer)
                        clearUp()
                        leanBack()
                    else:
                        messagebox.showerror("Error", "Pin Is Invalid", parent = transfer)
                except Exception as  es:
                    messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = transfer)

        transfer = Tk()
        transfer.title("Ice_Berg Mobile")
        transfer.maxsize(width = 500, height = 500)
        transfer.minsize(width = 500, height = 500)

        heading = Label(transfer, text = "Welcome To Ice_Berg Mobile", font = "Candara 25 bold")
        heading.place(x = 40, y = 150)

        label0001 = Label(transfer, text = "Enter Beneficiary Account Number :", font = "Candara 10 bold")
        label0001.place(x = 30, y = 220)
        
        label0002 = Label(transfer, text = "Enter Amount To Transfer:", font = "Candara 10 bold")
        label0002.place(x = 30, y = 260)

        label0003 = Label(transfer, text = "Enter Your Transaction Pin :", font = "Candara 10 bold")
        label0003.place(x = 30, y = 300)

        beneficiaryAcNo = StringVar()
        tranferAmnt = StringVar()
        transferPin = StringVar()

        beneficiary = Entry(transfer, width = 35, textvariable = beneficiaryAcNo)
        beneficiary.place(x = 250, y = 223)

        amntToTransfer = Entry(transfer, width = 35, textvariable = tranferAmnt)
        amntToTransfer.place(x = 250, y = 260)

        transfPin = Entry(transfer, width = 35 , show = "*", textvariable = transferPin)
        transfPin.place(x = 250, y = 297)

        btn_cnfrm = Button(transfer, text = "Confirm Transfer", font = "Candara 10 bold", command = confirmTransfer) #command is missing
        btn_cnfrm.place(x = 150, y = 334)

        btn_clear = Button(transfer, text = "Clear", font = "Candara 10 bold", command = clearUp) #command is missing
        btn_clear.place(x = 300, y = 334)

        rtrnBck = Button(transfer, text = "<-- Back", command = leanBack) #command is missing
        rtrnBck.place(x = 360, y = 20)

        transfer.mainloop()

    bank = Tk()#instantiation
    bank.title("Ice_Berg Mobile")
    bank.maxsize(width = 500, height = 500)
    bank.minsize(width = 500, height = 500)

    heading = Label(bank, text = "Welcome To Ice_Berg Mobile", font = "Candara 25 bold")
    heading.place(x = 40, y = 150)

    acc_info = Button(bank, text = "View Account Info", font = "Candara 10 bold", padx=45, command = account_info)# awaiting action
    acc_info.place(x = 150, y = 223)

    deposit = Button(bank, text = "Deposit To Your Acccount", font = "Candara 10 bold", padx=25, command = depositFunds)# awaiting action
    deposit.place(x = 150, y = 263)

    withdraw = Button(bank, text = "Withdraw From Your Acccount", font = "Candara 10 bold", padx=11, command = withdrawFunds)# awaiting action
    withdraw.place(x = 150, y = 303)

    transfer = Button(bank, text = "Transfer To Another Acccount", font = "Candara 10 bold", padx=13, command = transferFunds)# awaiting action
    transfer.place(x = 150, y = 343)

    logOut = Button(bank, text = "LOG OUT", command = log_out) #command missing
    logOut.place(x = 350, y = 20)



    bank.mainloop()

def signup():
    def action():
        if fname.get() == "" or lname.get() == "" or email.get() == "" or mobile_no.get() == "" or password.get == "" or very_pass.get() == "" or transact_pin.get() == "":
            messagebox.showerror("Error", "All Fields Are Required",  parent = registerwindow)
        elif '@' not in email.get():
            messagebox.showerror("Error", "Email Is Invalid", parent = registerwindow)
        elif mobile_no.get().__len__() != 11 and mobile_no.get().isdigit() == False:
            messagebox.showerror("Error", "Mobile Number Is Invalid", parent = registerwindow)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password And Verify Password Must Be The Same", parent = registerwindow)
        elif transact_pin.get().isdigit() == False:
            messagebox.showerror("Error", "Transaction Pin Must Be Digits", parent = registerwindow)
        elif transact_pin.get().__len__() != 4:
            messagebox.showerror("Error", "Transaction Pin Must Be Exactly 4 Digits", parent = registerwindow)
        else:
            try:
                firsName = fname.get()
                lasName = lname.get()
                email1 = email.get()
                mobile = mobile_no.get()
                passw = password.get()
                pin = transact_pin.get()


                result = create_user(firsName, lasName, email1, mobile, passw, pin)
                if result:
                    messagebox.showinfo("Success", "Registration Successful", parent = registerwindow)
                    clear()
                    switch()
                else:
                    messagebox.showerror("Error", "User Already Exists", parent = registerwindow)
            except Exception as  es:
                messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = registerwindow)

    def switch():
        registerwindow.destroy()

    def clear():
        email.delete("0", "end")
        password.delete("0", "end")
        very_pass.delete("0", "end")

    registerwindow = Tk()
    registerwindow.title("Ice_Berg Mobile")
    registerwindow.maxsize(width = 500, height = 600)
    registerwindow.minsize(width = 500, height = 600)

    heading = Label(registerwindow, text = "Register", font = "Candara 25 bold")
    heading.place(x = 80, y = 150)

    fname = Label(registerwindow, text = "First Name :", font = "Candara 10 bold")
    fname.place(x = 80, y = 220)

    lname = Label(registerwindow, text = "Last Name :", font = "Candara 10 bold")
    lname.place(x = 80, y = 260)

    email = Label(registerwindow, text = "Email :", font = "Candara 10 bold")
    email.place(x = 80, y = 300)

    mobile_no = Label(registerwindow, text = "Mobile Number :", font = "Candara 10 bold")
    mobile_no.place(x = 80, y = 340)

    password = Label(registerwindow, text = "Password :", font = "Candara 10 bold")
    password.place(x = 80, y = 380)

    very_pass = Label(registerwindow, text = "Verify Password :", font = "Candara 10 bold")
    very_pass.place(x = 80, y = 420)

    transact_pin = Label(registerwindow, text = "Transaction Pin :", font = "Candara 10 bold")
    transact_pin.place(x = 80, y = 460)

    fname = StringVar()
    lname = StringVar()
    email = StringVar()
    mobile_no = StringVar()
    password = StringVar()
    very_pass = StringVar()
    transact_pin = StringVar()

    fname = Entry(registerwindow, width = 40, textvariable = fname)
    fname.place(x = 200, y = 223)

    lname = Entry(registerwindow, width = 40, textvariable = lname)
    lname.place(x = 200, y = 260)

    email = Entry(registerwindow, width = 40, textvariable = email)
    email.place(x = 200, y = 297)

    mobile_no = Entry(registerwindow, width = 40, textvariable = mobile_no)
    mobile_no.place(x = 200, y = 339)

    password = Entry(registerwindow, width = 40, textvariable = password)
    password.place(x = 200, y = 380)

    very_pass = Entry(registerwindow, width = 40, textvariable = very_pass)
    very_pass.place(x = 200, y = 418)

    transact_pin = Entry(registerwindow, width = 40, textvariable = transact_pin)
    transact_pin.place(x = 200, y = 458)

    btn_signup = Button(registerwindow, text = "Signup", font = "Candara 10 bold", command = action) #command is missing
    btn_signup.place(x = 200, y = 485)

    btn_login = Button(registerwindow, text = "Clear", font = "Candara 10 bold", command = clear) #command is missing
    btn_login.place(x = 260, y = 485)

    switchLogin = Button(registerwindow, text = "Switch To Login", command = switch) #command is missing
    switchLogin.place(x = 350, y = 20)

    registerwindow.mainloop()

home()