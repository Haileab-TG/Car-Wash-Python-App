# Program Name: CleanCar.com GUI Module
# Author: Haileab Tesfamaryam Goitum
# Date of Creation:  5 DEC 2020

from tkinter import *
from tkinter import messagebox
import csv
from CarWash_System import WebUser


# GUI Classes

class LoginPage:
    '''Class to reprsent login page'''

    # intializer
    def __init__(self, master, user=WebUser ):
        self.user = user
        self.master = master
        self.master.title("CleanCar Login")

        self.lblTitle = Label(self.master, font= 'Times 16 bold italic', text="Welcome To CleanCar.com", bg="#292a2b", fg="#E9E5C2", width=55,
                              height=4, anchor='center')
        self.lblTitle.grid(columnspan=6)


        self.lbluserName = Label(self.master, font= 'Times 11 bold italic', text="Username")
        self.lbluserName.grid(row=2, column=0, pady=30)


        self.entUsername = Entry(self.master, width=40)
        self.entUsername.grid(row=2, column=1, pady=30, columnspan=2)

        self.lblPassword = Label(self.master, font= 'Times 11 bold italic', text="Password")
        self.lblPassword.grid(row=3, column=0)


        self.entPassword = Entry(self.master, width=40)
        self.entPassword.grid(row=3, column=1, columnspan=2)

        self.btnLogin = Button(self.master, font= 'Times 11 bold italic',text="Login", width=10, bg="#292a2b", fg="#E9E5C2", command=self.validator)
        self.btnLogin.grid(row=4, column=1, pady=30)


        self.btnSignUp = Button(self.master, text="Sign Up", font= 'Times 11 bold italic',width=10, bg="#292a2b", fg="#E9E5C2",
                                command=self.gotoSignupPage)
        self.btnSignUp.grid(row=4, column=2, pady=30)


        self.lblBottom = Label(self.master, font= 'Times 16 bold italic',text="Life is Easy with CleanCar.com", bg="#292a2b", fg="#E9E5C2", width=55,
                               height=2, anchor='center')
        self.lblBottom.grid(columnspan=6, row=6)


    def gotoSignupPage(self):
        self.root2 = Toplevel(self.master)
        self.signUpPage = SignUpPage(self.root2, self.master, self.user)
        self.master.withdraw()

    def gotoHomepage(self):
        self.root2 = Toplevel(self.master)
        self.homepage = HomePage(self.root2, self.master, self.user)
        self.master.withdraw()
        self.entUsername.delete(0, 'end')
        self.entPassword.delete(0, 'end')

    def validator(self):
        if self.entPassword.get() and self.entUsername.get():
            if self.checkCredetial():
                self.user.login(self.entUsername.get(), self.entPassword.get())
                self.gotoHomepage()
            else:
                messagebox.showerror("Wrong Credential", "Incorrent username or password")
        else:
            messagebox.showerror("Missing Mandatories", "Please Enter Username and Password")

    def checkCredetial(self):
        try:
            with open('webuser.csv', 'r') as re:
                readfile = csv.reader(re)
                for i in readfile:
                    if i[1] == self.entUsername.get() and i[2] == self.entPassword.get():
                        return True
                return False
        except:
            messagebox.showerror("File Not Found", "Records and WebUser Files Not Found, Please place the text files submited with this codes on the same directory")


class SignUpPage:
    '''Class to reprsent signup page'''

    # initializer
    def __init__(self, master, loginpage=LoginPage, webuser= WebUser):
        self.webUser= webuser
        self.loginpage = loginpage
        self.signUpPage = master
        self.signUpPage.title("CleanCar Signup")




        self.lblTitle = Label(self.signUpPage, font= 'Times 14 bold italic',text="Signup for CleanCar.com", bg="#292a2b", fg="#E9E5C2", width=55,
                              height=4, anchor='center')
        self.lblTitle.grid(columnspan=6, pady=30)


        # signup options as user, regular employee or manager
        self.lblInfom = Label(self.signUpPage, font= 'Times 11 bold italic', text="Sign Up As: ", width=40)
        self.lblInfom.grid(row=1, columnspan=2)


        # signup option radio buttons variable initializing
        self.var = StringVar()

        # user, regular employee and manager radio buttons
        self.rdRegMem= Radiobutton(self.signUpPage, text="Regular Member", value='Regular Member', variable=self.var, tristatevalue=0)
        self.rdRegMem.grid(row=2, column=1, sticky=W)

        self.rdSliverMem = Radiobutton(self.signUpPage, text="Silver Member", value='Silver Member', variable=self.var, tristatevalue=0)
        self.rdSliverMem.grid(row=3, column=1, sticky=W)

        self.rdGoldMem = Radiobutton(self.signUpPage, text="Gold Member", value='Gold Member', variable=self.var, tristatevalue=0)
        self.rdGoldMem.grid(row=4, column=1, sticky=W)

        self.rdregEmp = Radiobutton(self.signUpPage, text="Employee", value='Employee', variable=self.var,
                                    tristatevalue=0)
        self.rdregEmp.grid(row=5, column=1, sticky=W)

        self.rdManger = Radiobutton(self.signUpPage, text="Manager", value='Manager', variable=self.var, tristatevalue=0)
        self.rdManger.grid(row=6, column=1, sticky=W)

        self.lblfullName = Label(self.signUpPage, font= 'Times 11 bold italic',text="Fullname:")
        self.lblfullName.grid(row=7, column=0)

        self.entfullname = Entry(self.signUpPage, width=40)
        self.entfullname.grid(row=7, column=1, columnspan=2)

        self.lbluserName = Label(self.signUpPage, font= 'Times 11 bold italic', text="Username:")
        self.lbluserName.grid(row=8, column=0)

        self.entUsername = Entry(self.signUpPage, width=40)
        self.entUsername.grid(row=8, column=1, columnspan=2)

        self.lblAddress = Label(self.signUpPage, font= 'Times 11 bold italic',text="Address:")
        self.lblAddress.grid(row=9, column=0)

        self.entAddress = Entry(self.signUpPage, width=40)
        self.entAddress.grid(row=9, column=1, columnspan=2)

        self.lblEmail = Label(self.signUpPage, font= 'Times 11 bold italic', text="Email:")
        self.lblEmail.grid(row=10, column=0)

        self.entEmail = Entry(self.signUpPage, width=40)
        self.entEmail.grid(row=10, column=1, columnspan=2)

        self.lblPhoneNum = Label(self.signUpPage,font= 'Times 11 bold italic', text="Phone Num:")
        self.lblPhoneNum.grid(row=11, column=0)

        self.entPhoneNum = Entry(self.signUpPage, width=40)
        self.entPhoneNum.grid(row=11, column=1, columnspan=2)

        self.lblPassword = Label(self.signUpPage, font= 'Times 11 bold italic', text="Password:")
        self.lblPassword.grid(row=12, column=0)

        self.entPassword = Entry(self.signUpPage, width=40)
        self.entPassword.grid(row=12, column=1, columnspan=2)

        self.lblConPassword = Label(self.signUpPage,font= 'Times 11 bold italic', text="Confirm Password:")
        self.lblConPassword.grid(row=13, column=0)

        self.entConPassword = Entry(self.signUpPage, width=40)
        self.entConPassword.grid(row=13, column=1, columnspan=2)

        self.btnSignUp = Button(self.signUpPage, font= 'Times 11 bold italic',text="Sign Up", width=10, bg="#292a2b", fg="#E9E5C2",
                                command=self.validator)
        self.btnSignUp.grid(row=14, column=3, pady=30)


        self.btnBack = Button(self.signUpPage, font= 'Times 11 bold italic',text="Back", width=10, bg="#292a2b", fg="#E9E5C2", command=self.back)
        self.btnBack.grid(row=14, column=0, pady=30)


        self.lblBottom = Label(self.signUpPage, font= 'Times 14 bold italic',text="Life is Easy with CleanCar.com", bg="#292a2b", fg="#E9E5C2",
                               width=55, height=2, anchor='center')
        self.lblBottom.grid(columnspan=6, row=15)


    def back(self):
        self.loginpage.deiconify()
        self.signUpPage.destroy()

    def validator(self):

        if self.entfullname.get() and self.entUsername.get() and self.entPassword.get() and self.entEmail.get() and self.entAddress.get() and self.entPhoneNum.get() and self.var.get():
            if self.entPassword.get() != self.entConPassword.get():
                messagebox.showerror("Unmatching Passowrd", "Password not same, retype it please")
            else:
                if self.checkUserNameExistance():
                    messagebox.showerror("Username Exist", "Username already exist, Please try another")
                else:
                    self.webUser.Register(self.entUsername.get(), self.entPassword.get(), self.var.get(), self.entAddress.get(), self.entEmail.get(), self.entPhoneNum.get(), self.entfullname.get())
                    self.back()
        else:
            messagebox.showerror("Missing Mandatories", "All Fields Must Fill")


    # check if user name already used
    def checkUserNameExistance(self):
        try:
            with open('WebUser.csv', 'r') as re:
                readfile = csv.reader(re)
                for i in readfile:
                    if i[1] == self.entUsername.get():
                        return True
        except:
            messagebox.showerror("File Not Found", "Records and WebUser Files Not Found, Please place the text files submited with this codes on the same directory")


class HomePage:
    '''Class to reprsent login page'''

    # intializer
    def __init__(self, master, loginpage=LoginPage, webuser= WebUser):
        self.loginPage = loginpage
        self.master = master
        self.master.title("CleanCar Login")
        self.webuser= webuser



        self.lblTitle = Label(self.master, font= 'Times 14 bold italic',text="CleanCar.com Home Page", bg="#292a2b", fg="#E9E5C2", width=60,
                              height=5,
                              anchor='center')
        self.lblTitle.grid(columnspan=3, rowspan=2)


        self.welcomeUser = Label(self.master, font= 'Times 13 bold italic', text='Welcome ' + self.webuser.getUserName(),  bg="#292a2b", fg="#E9E5C2",
                                 width=60,
                                 anchor='center')
        self.welcomeUser.grid(columnspan=3, rowspan=2, row=1)

        # buttons
        self.specialprivilege = Button(self.master, text="Special Privilege", font="Times 11 bold italic", width=15, bg="#292a2b", fg="#E9E5C2", command= self.special)
        self.specialprivilege.grid(row=1, column=0, rowspan=2, sticky="w", padx=60)


        self.btnUserInfo = Button(self.master, font= 'Times 11 bold italic',text="User Info", width=7, bg="#292a2b", fg="#E9E5C2", command= self.gotoUserInfoPage)
        self.btnUserInfo.grid(row=1, column=2, rowspan=2)


        self.btnLogout = Button(self.master, font= 'Times 11 bold italic',text="Logout", width=7, bg="#292a2b", fg="#E9E5C2", command=self.logout)
        self.btnLogout.grid(row=0, column=2, sticky=E)


        # service title
        self.lblService = Label(self.master, font= 'Times 11 bold italic',text="Service and Their price", anchor='center')
        self.lblService.grid(row=3, column=0, columnspan=3)


        # the checkboxes
        self.regWash = StringVar()
        self.selfWash = StringVar()
        self.steamWash = StringVar()
        self.touchWash = StringVar()
        self.detailWash = StringVar()

        # title
        self.lblService = Label(self.master,font= 'Times 11 bold italic', text="Service", anchor='center')
        self.lblService.grid(row=4, column=0, sticky="w", padx=60)


        # checkbox
        self.cbRegWSH = Checkbutton(self.master, text="Regular Wash", variable=self.regWash, onvalue="Regular Wash", offvalue="0",
                              tristatevalue=0)
        self.cbRegWSH.grid(row=5, column=0, sticky="w", padx=60)

        self.cbSteamWSH = Checkbutton(self.master, text="Steam Wash", variable=self.steamWash, onvalue="Steam Wash", offvalue="0",
                              tristatevalue=0)
        self.cbSteamWSH.grid(row=6, column=0, sticky="w", padx=60)

        self.cbDetailWSH = Checkbutton(self.master, text="Detailing Wash", variable=self.detailWash, onvalue="Detailing Wash", offvalue="0",
                              tristatevalue=0)
        self.cbDetailWSH.grid(row=7, column=0, sticky="w", padx=60)

        self.cbTouchlessWSH = Checkbutton(self.master, text="Touchless Wash", variable=self.touchWash, onvalue="Touchless Wash", offvalue="0",
                              tristatevalue=0)
        self.cbTouchlessWSH.grid(row=8, column=0, sticky="w", padx=60)

        self.cbSelfWSH = Checkbutton(self.master, text="Self-Service,Try washing on your own", variable=self.selfWash, onvalue="self-wash", offvalue="0",
                              tristatevalue=0)
        self.cbSelfWSH.grid(row=9, column=0, sticky="w", padx=60)

        # price Labels
        self.lblService = Label(self.master, font= 'Times 11 bold italic',text="Prices", anchor='center')
        self.lblService.grid(row=4, column=1, columnspan=6)


        self.regWSHPrice = Label(self.master, text="40 aed", anchor='center')
        self.regWSHPrice.grid(row=5, column=1, columnspan=6)


        self.steamPrice = Label(self.master, text="100 aed", anchor='center')
        self.steamPrice.grid(row=6, column=1, columnspan=6)


        self.detailPrice = Label(self.master, text="70 aed", anchor='center')
        self.detailPrice.grid(row=7, column=1, columnspan=6)


        self.touchlessPrice = Label(self.master, text="90 aed", anchor='center')
        self.touchlessPrice.grid(row=8, column=1, columnspan=6)


        self.selfWSHPrice = Label(self.master, text="20 aed", anchor='center')
        self.selfWSHPrice.grid(row=9, column=1, columnspan=6)


        # add to cart button
        self.btnAddtocart = Button(self.master, font= 'Times 11 bold italic',text="Add to Cart", width=10, bg="#292a2b", fg="#E9E5C2", command= self.gotoPaymentPage)
        self.btnAddtocart.grid(row=10, column=0, columnspan=3, pady=10)


        # total balance, top-up and wash-card number
        self.lblBalance = Label(self.master, font= 'Times 11 bold italic', text="Available Balance", anchor='center')
        self.lblBalance.grid(row=11, column=1)


        self.lblValueBalance = Label(self.master, font= 'Times 11 bold italic',text= self.webuser.getWashCard().getBalance(), anchor='center')
        self.lblValueBalance.grid(row=12, column=1)


        self.btnTopup = Button(self.master,font= 'Times 11 bold italic', text="Top-up", width=10, bg="#292a2b", fg="#E9E5C2",
                               command=self.gotoTopupPage)
        self.btnTopup.grid(row=11, column=2)


        self.lblAssign = Label(self.master,font= 'Times 11 bold italic', text="Assigned Card Number", anchor='center')
        self.lblAssign.grid(row=11, column=0)


        self.lblWSCNum = Label(self.master, font= 'Times 11 bold italic',text=self.webuser.getWashCard().getCardNum(), anchor='center')
        self.lblWSCNum.grid(row=12, column=0)


        self.lblprintwscardNum = Label(self.master, font='bold 15',
                                       text="Please Pick Your Washing Card, if haven't yet, Thank You!", fg='red',
                                       anchor='center')
        self.lblprintwscardNum.grid(row=13, column=0, columnspan=3, pady=10)


        self.lblBottom = Label(self.master, font= 'Times 13 bold italic',text="Life is Easy with CleanCar.com", bg="#292a2b", fg="#E9E5C2", width=66,
                               height=1, anchor='center')
        self.lblBottom.grid(columnspan=3, row=14)


    # Logout method
    def logout(self):
        self.loginPage.deiconify()
        self.master.destroy()

    def gotoTopupPage(self):
        self.root2 = Toplevel(self.master)
        self.topupPage = TopUpPage(self.root2, self.master, self.webuser)
        self.master.withdraw()

    def gotoUserInfoPage(self):
        self.root2 = Toplevel(self.master)
        self.userInfoPage = UserInfo(self.root2, self.master, self.webuser)
        self.master.withdraw()

    def gotoPaymentPage(self):
        if self.regWash.get() or self.selfWash.get() or self.steamWash.get() or self.touchWash.get() or self.detailWash.get():
            self.webuser.purchase(self.regWash.get(), self.steamWash.get(), self.detailWash.get(), self.touchWash.get(), self.selfWash.get())
            self.root2= Toplevel(self.master)
            self.paymentPage= PaymentPage(self.root2, self.master, self.webuser)
            self.master.withdraw()
        else:
            messagebox.showerror("Missing Mandatories", "Nothing Selected")

    # method to navigate to special privilege
    def special(self):
        if self.webuser.getAccountType() == 'Employee' or self.webuser.getAccountType() == 'Manager':
            self.root2 = Toplevel(self.master)
            self.specialprvilage = SpecialPrivilage(self.root2, self.master, self.webuser)
            self.master.withdraw()
        else:
            messagebox.showerror("Alert", "User doesn't have sepcial privilage, it is only for Employees and Managers")


class TopUpPage:
    '''Class to reprsent login page'''

    # intializer
    def __init__(self, master, homepage=HomePage, user= WebUser):
        self.webuser= user
        self.homepage = homepage
        self.master = master
        self.master.title("CleanCar Login")
        # self.master.geometry("600x1000")
        # # self.master.resizable(0, 0)



        # Page Header
        self.lblHeader = Label(self.master,font= 'Times 14 bold italic', text="Top-up Page", bg="#292a2b", fg="#E9E5C2", width=86,
                               height=3, anchor='center')
        self.lblHeader.grid(columnspan=12)


        # the title
        self.title = Label(self.master, text="Top Up Using Visa, Master, Debit or Credit Cards of Any Bank", font='Times 11 bold italic')
        self.title.grid(row=1, column=0, padx=60, columnspan=12)

        self.labelFname = Label(self.master, text="Name on Card")
        self.labelFname.grid(row=2, column=0, sticky=W, padx=80)
        self.fNameEntry = Entry(self.master, width=30)
        self.fNameEntry.grid(columnspan=2, row=2, column=1, pady="10")

        self.labelCnum = Label(self.master, text="Card Number:")
        self.labelCnum.grid(row=3, column=0, sticky=W, padx=80)
        self.entryCnum = Entry(self.master, width= 30)
        self.entryCnum.grid(columnspan=2, row=3, column=1, pady="10")

        self.labelExpDate = Label(self.master, text="Expiration Date:")
        self.labelExpDate.grid(row=4, column=0, sticky=W, padx=80)
        self.entryExpDate = Entry(self.master, width=30)
        self.entryExpDate.grid(columnspan=2, row=4, column=1, pady="10")

        self.labelcvv = Label(self.master, text="CVV:")
        self.labelcvv.grid(row=5, column=0, sticky=W, padx=80)
        self.entrycvv = Entry(self.master, width=30)
        self.entrycvv.grid(columnspan=2, row=5, column=1, pady="10")

        self.labelAmt = Label(self.master, text="Amount")
        self.labelAmt.grid(row=6, column=0, sticky=W, padx=80)
        self.entryAmt = Entry(self.master, width=30)
        self.entryAmt.grid(columnspan=2, row=6, column=1, pady="10")


        self.labelWSCnum = Label(self.master, text="Wash-card Number:")
        self.labelWSCnum.grid(row=7, column=0, sticky=W, padx=80)
        self.entryWSCnum = Label(self.master, text= self.webuser.washCard.getCardNum())
        self.entryWSCnum.grid(columnspan=2, row=7, column=1, pady="10")

        # buttons
        self.btnTopup = Button(self.master, text="TopUp", width=10, bg="#292a2b", fg="#E9E5C2", command= self.TopUp)
        self.btnTopup.grid(row=8, column=1, pady=20)

        self.lblinfoLoc = Text(self.master, font='bold 15', fg='red', width= 45, height= 3, wrap= WORD)
        self.lblinfoLoc.grid(row=9, column=1,  pady=10)
        self.lblinfoLoc.configure(state= 'normal')
        self.lblinfoLoc.insert(END, "Want Topup by Cash, Get our topup machine in our store Location(Abu Dhabi, Hamdan street, block= 123, Garage=1, Floor=2")
        self.lblinfoLoc.configure(state= 'disabled')

        # footer
        self.lblBottom = Label(self.master,font= 'Times 13 bold italic', text="Life is Easy with CleanCar.com", bg="#292a2b", fg="#E9E5C2", width=95,
                               height=2, anchor='center')
        self.lblBottom.grid(columnspan=10, row=10)




    def TopUp(self):
        if self.entryAmt.get() and self.entryCnum.get() and self.entrycvv.get() and self.entryExpDate.get() and self.fNameEntry.get():
            try:
                amt= float(self.entryAmt.get())
                if amt <= 0:
                    raise ValueError
            except:
                messagebox.showerror("Alert", "Amount should be any number above 0")
            else:
                self.webuser.topup(amt)
                messagebox.showerror("Info", "Now the app will quit. Run it and Login again. Then lets buy our services")
                quit()
        else:
            messagebox.showerror("Missing Mandatories", "All Fields must be filled")


class PaymentPage:
    '''Class to reprsent login page'''

    # intializer
    def __init__(self, master, hompage= HomePage, user= WebUser):
        self.hompage= hompage
        self.webuser= user
        self.master = master
        self.master.title("CleanCar Payment")

        self.lblTitle = Label(self.master, font= 'Times 14 bold italic', text="Payment Page", bg="#292a2b", fg="#E9E5C2", width=55,
                              height=3, anchor='center')
        self.lblTitle.grid(columnspan=12)


        # the labels
        self.labelGrand = Label(self.master, font='Times 11 bold italic',text="Grand Total & discount")
        self.labelGrand.grid(row=1, column=1, columnspan=4)
        self.labelGrandTotal = Label(self.master, width= 50, text= 'Before Discount '+ str(self.webuser.totalbeforeDiscount()) + ' AED,    After Discount '+ str(self.webuser.totalAfterDiscount(self.webuser.discount(), self.webuser.totalbeforeDiscount()))+' AED')
        self.labelGrandTotal.grid(row=2, column=1, columnspan=4)

        self.labelInCart = Label(self.master, font= 'Times 11 bold italic',text="In Cart")
        self.labelInCart.grid(row=3, column=1, columnspan=4)
        self.txtInCart = Text(self.master, width = 30, height= 8, wrap= WORD)
        self.txtInCart.configure(state= 'normal')
        self.txtInCart.insert(END, self.webuser.namePuchasedService())
        self.txtInCart.configure(state= 'disabled')
        self.txtInCart.grid(row=4, column=1, columnspan=4)

        self.labelWSCnum = Label(self.master, font= 'Times 11 bold italic',text="Wash-card Number:")
        self.labelWSCnum.grid(row=5, column=0)
        self.entryWSCnum = Label(self.master,text= self.webuser.washCard.getCardNum(), width=30)
        self.entryWSCnum.grid(columnspan=2, row=5, column=1, pady="10")

        # Top up button
        self.btnTopup = Button(self.master, text="Top Up", width=10, bg="#292a2b", fg="#E9E5C2", command=self.gotoTopupPage)
        self.btnTopup.grid(row=6, column=7, pady=20)

        #pay button
        self.btnPay = Button(self.master, text="Pay", width=10, bg="#292a2b", fg="#E9E5C2", command= self.Pay)
        self.btnPay.grid(row=6, column=1, pady=20)

        # footer
        self.lblBottom = Label(self.master, font= 'Times 14 bold italic',text="Life is Easy with CleanCar.com", bg="#292a2b", fg="#E9E5C2", width=55,
                               height=2, anchor='center')
        self.lblBottom.grid(columnspan=10, row=7)


    def gotoTopupPage(self):
        self.root2 = Toplevel(self.master)
        self.topupPage = TopUpPage(self.root2, self.master, self.webuser)
        self.master.withdraw()
    def Pay(self):
        self.webuser.pay()


class UserInfo:
    '''Class to reprsent signup page'''

    # initializer
    def __init__(self, master, home= HomePage, user= WebUser):
        self.homepage= home
        self.webuser= user
        self.userInfoPage = master
        self.userInfoPage.title("CleanCar User Info")


        self.lblTitle = Label(self.userInfoPage, font= 'Times 14 bold italic',text="CleanCar.com User Info", bg="#292a2b", fg="#E9E5C2", width=55,
                              height=4, anchor='center')
        self.lblTitle.grid(columnspan=6, pady=30)



        self.lblfullName = Label(self.userInfoPage,font= 'Times 11 bold italic', text="Fullname:")
        self.lblfullName.grid(row=7, column=0)

        self.entfullname = Entry(self.userInfoPage, width=40)
        self.entfullname.grid(row=7, column=1, columnspan=2)
        self.entfullname.insert(END, self.webuser.getFullname())

        self.lbluserName = Label(self.userInfoPage, font= 'Times 11 bold italic',text="Username:")
        self.lbluserName.grid(row=8, column=0)

        self.entUsername = Entry(self.userInfoPage, width=40)
        self.entUsername.grid(row=8, column=1, columnspan=2)
        self.entUsername.insert(END, self.webuser.getUserName())

        self.lblAddress = Label(self.userInfoPage,font= 'Times 11 bold italic', text="Address:")
        self.lblAddress.grid(row=9, column=0)

        self.entAddress = Entry(self.userInfoPage, width=40)
        self.entAddress.grid(row=9, column=1, columnspan=2)
        self.entAddress.insert(END, self.webuser.getaddress())

        self.lblEmail = Label(self.userInfoPage, font= 'Times 11 bold italic',text="Email:")
        self.lblEmail.grid(row=10, column=0)

        self.entEmail = Entry(self.userInfoPage, width=40)
        self.entEmail.grid(row=10, column=1, columnspan=2)
        self.entEmail.insert(END, self.webuser.getEmail())

        self.lblPhoneNum = Label(self.userInfoPage, font= 'Times 11 bold italic',text="Phone Num:")
        self.lblPhoneNum.grid(row=11, column=0)

        self.entPhoneNum = Entry(self.userInfoPage, width=40)
        self.entPhoneNum.grid(row=11, column=1, columnspan=2)
        self.entPhoneNum.insert(END, self.webuser.getPhoneNum())

        self.lblPassword = Label(self.userInfoPage,font= 'Times 11 bold italic', text="Password:")
        self.lblPassword.grid(row=12, column=0)

        self.entPassword = Entry(self.userInfoPage, width=40)
        self.entPassword.grid(row=12, column=1, columnspan=2)
        self.entPassword.insert(END, self.webuser.getPassword())

        self.lblConPassword = Label(self.userInfoPage, font= 'Times 11 bold italic',text="Confirm Password:")
        self.lblConPassword.grid(row=13, column=0)

        self.entConPassword = Entry(self.userInfoPage, width=40)
        self.entConPassword.grid(row=13, column=1, columnspan=2)

        self.lblTitleCarNum = Label(self.userInfoPage,font= 'Times 11 bold italic',text="Card Number:")
        self.lblTitleCarNum.grid(row=14, column=0)
        self.lblCarNum = Label(self.userInfoPage,text=self.webuser.washCard.getCardNum(), width=40)
        self.lblCarNum.grid(row=14, column=1, columnspan= 2)

        self.lblTitleBalance = Label(self.userInfoPage,font= 'Times 11 bold italic',text="Balance:")
        self.lblTitleBalance.grid(row=15, column=0)
        self.lblBalance = Label(self.userInfoPage,text=self.webuser.washCard.getBalance(), width=40)
        self.lblBalance.grid(row=15, column=1, columnspan= 2)

        self.lblTiltlelpts = Label(self.userInfoPage,font= 'Times 11 bold italic',text="Points:")
        self.lblTiltlelpts.grid(row=16, column=0)
        self.lblpts = Label(self.userInfoPage,text=self.points(), width=40)
        self.lblpts.grid(row=16, column=1, columnspan= 2)

        self.btnUpdate = Button(self.userInfoPage, font= 'Times 11 bold italic',text="Update", width=10, bg="#292a2b", fg="#E9E5C2", command= self.validator)
        self.btnUpdate.grid(row=17, column=3, pady=30)


        self.btnBack = Button(self.userInfoPage, font= 'Times 11 bold italic',text="Back", width=10, bg="#292a2b", fg="#E9E5C2", command= self.back)
        self.btnBack.grid(row=17, column=0, pady=30)


        self.lblBottom = Label(self.userInfoPage, font= 'Times 14 bold italic',text="Life is Easy with CleanCar.com", bg="#292a2b", fg="#E9E5C2",
                               width=55, height=2, anchor='center')
        self.lblBottom.grid(columnspan=6, row=18)



    # method to back from userInfo Page to homepage
    def back(self):
        self.homepage.deiconify()
        self.userInfoPage.destroy()

    # show points
    def points(self):
        if self.webuser.getAccountType() == 'Gold Memeber' or self.webuser.getAccountType() == 'Silver Member':

                return self.webuser.washCard.getPoint()
        else:
            return 'Not Applicable'

    # method to validate user info updation
    def validator(self):
        if self.entfullname.get() and self.entUsername.get() and self.entPassword.get() and self.entEmail.get() and self.entAddress.get() and self.entPhoneNum.get():
            if self.entPassword.get() != self.entConPassword.get():
                messagebox.showerror("Unmatching Passowrd", "Password not same, retype it please")
            else:
                if self.checkUserNameExistance():
                    messagebox.showerror("Username Exist", "Username already exist, Please try another")
                else:
                    self.webuser.updateInfo(self.entfullname.get(), self.entUsername.get(), self.entPassword.get(),
                                          self.entAddress.get(), self.entEmail.get(), self.entPhoneNum.get() )
                    self.back()
        else:
            messagebox.showerror("Missing Mandatories", "All Fields Must Fill")


    # check if user name already used
    def checkUserNameExistance(self):
        try:
            with open('WebUser.csv', 'r') as re:
                readfile = csv.reader(re)
                for i in readfile:
                    if i[1] == self.entUsername.get() and self.webuser.getUserName() != self.entUsername.get():
                        return True
        except:
            messagebox.showerror("File Not Found", "Records and WebUser Files Not Found, Please place the text files submited with this codes on the same directory")


class SpecialPrivilage:
    '''Class to reprsent Special Privilage'''

    # initializer
    def __init__(self, master, homepage= HomePage, user= WebUser):
        self.homepage= homepage
        self.webuser= user
        self.userInfoPage = master
        self.userInfoPage.title("Special Priviliage")


        self.lblTitle = Label(self.userInfoPage, font= 'Times 14 bold italic',text="CleanCar.com Special Priviliage", bg="#292a2b", fg="#E9E5C2", width=70,
                              height=3, anchor='center')
        self.lblTitle.grid(columnspan=6, pady=30)


        self.txtListAll= Text(self.userInfoPage, width= 40, height= 20, wrap= WORD)
        self.txtListAll.grid(row= 1, column= 0, sticky= W, rowspan= 8)
        self.txtListAll.configure(state= 'normal')
        self.txtListAll.insert(END,  self.webuser.assingViewMan())
        self.txtListAll.configure(state= 'disabled')

        self.btnDelete = Button(self.userInfoPage,font= 'Times 11 bold italic', text="Delete all accounts", width=20, bg="#292a2b", fg="#E9E5C2", command= self.webuser.Delete)
        self.btnDelete.grid(row=3, column=3, sticky= W, pady= 30)

        self.btnBack = Button(self.userInfoPage,font= 'Times 11 bold italic', text="Back", width=10, bg="#292a2b", fg="#E9E5C2", command= self.back)
        self.btnBack.grid(row=3, column=2, sticky=W, pady=30)

    # method to back from userInfo Page to homepage
    def back(self):
        self.homepage.deiconify()
        self.userInfoPage.destroy()



