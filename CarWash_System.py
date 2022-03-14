# Program Name: CleanCar.com System
# Author: Haileab Tesfamaryam Goitum
# Date of Creation:  5 DEC 2020



# Program
from tkinter import messagebox
import csv
import os
import random


class CleanCarService:
    '''Class to represent services of CleanCar.com'''

    # Initializer
    def __init__(self, price=0.0, name=''):
        self.price = price
        self.serviceName = name

    # setter and getter
    def setServiceName(self, name):
        self.serviceName = name

    def getService(self):
        return self.serviceName

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


class RegularWash(CleanCarService):
    '''Class to represent regular car wash service of CleanCar.com'''

    # Initializer
    def __init__(self, name='Regular Wash', price=40, desc='Just a regular wash'):
        CleanCarService.__init__(self, price, name)
        self.desc = desc


class CarSteamWash(CleanCarService):
    '''Class to represent steam car wash service of CleanCar.com'''

    # Initializer
    def __init__(self, name='Steam Wash', price=100, desc='Waterless car wash for better shining'):
        CleanCarService.__init__(self, price, name)
        self.desc = desc


class CarDetailingWash(CleanCarService):
    '''Class to represent detailing car wash service of cleancar.com'''

    # Initializer
    def __init__(self, name='Detailing Wash', price=70, desc='Internal and external parts wash'):
        CleanCarService.__init__(self, price, name)
        self.desc = desc


class CarTouchLessWash(CleanCarService):
    '''Class to represent touch less car wash service of cleancar.com'''

    # Initializer
    def __init__(self, name='Touchless Wash', price=90, desc='Contactless car wash to prevent unwanted scratches'):
        CleanCarService.__init__(self, price, name)
        self.desc = desc


class SelfServiceWash(CleanCarService):
    '''Class to represent self car wash service of cleancar.com'''

    # Initializer
    def __init__(self, name='Self-wash', price=20, desc='Your chance to wash your car on your own'):
        CleanCarService.__init__(self, price, name)
        self.desc = desc


class WashCard():
    '''Class to represent car wash card of CleanCar.com'''

    # Initializer
    def __init__(self, WSHnum='', balance=0.0, points=0):
        # self.services = services
        self.washCardNum = WSHnum
        self.balance = balance
        self.points = points

    # setter and getter
    def setCardNum(self, num):
        self.washCardNum = num

    def getCardNum(self):
        return self.washCardNum

    def setBalance(self, bal):
        self.balance = bal

    def getBalance(self):
        return self.balance

    def setPoint(self, pon):
        self.points = pon

    def getPoint(self):
        return self.points


class WebUser():
    '''Class to represent all users of CleanCar.com'''

    # Initializer
    def __init__(self, userName='', password='', fullname='', address='', phone='', email='', userID=0, accType=''):
        self.washCard = WashCard
        self.username = userName
        self.password = password
        self.fullname = fullname
        self.address = address
        self.phonenum = phone
        self.email = email
        self.accountType = accType
        self.userID = userID
        self.purchasedSerivces = []

        # setter and getter methods

    def setUserName(self, userName):
        self.userName = userName

    def getUserName(self):
        return self.userName

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setFullname(self, fullname):
        self.fullname = fullname

    def getFullname(self):
        return self.fullname

    def setAddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def setPhoneNum(self, phone):
        self.phonenum = phone

    def getPhoneNum(self):
        return self.phonenum

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setAccountType(self, accountType):
        self.accountType = accountType

    def getAccountType(self):
        return self.accountType

    def setUserID(self, id):
        self.userID = id

    def getUserID(self):
        return self.userID

    def setWashCard(self, card):
        self.washCard = card

    def getWashCard(self):
        return self.washCard

    def setPurchasedService(self, ser):
        self.purchasedSerivces = ser

    def getPurchasedService(self):
        return self.purchasedSerivces

    # method to register new regular user to record.txt file and set attributes of this class
    def Register(self, username, password, accountType, address, email, phone, fullname):
        # Setting user attributes
        self.setUserName(username)
        self.setPassword(password)
        self.setAccountType(accountType)
        self.setAddress(address)
        self.setEmail(email)
        self.setPhoneNum(phone)
        self.setFullname(fullname)

        # recording username and password to webuser file
        with open('WebUser.csv', 'a', newline='') as pl:

            writer = csv.writer(pl)

            # return the last ID
            def LastID():
                if os.path.getsize('WebUser.csv') == 0:
                    return 0
                else:
                    lastID = 0
                    with open('WebUser.csv', 'r') as re:
                        readfile = csv.reader(re)
                        for i in readfile:
                            if int(i[0]) > int(lastID):
                                lastID = i[0]
                        return int(lastID) + 1

            self.setUserID(LastID())
            writer.writerow([self.getUserID(), self.getUserName(), self.getPassword()])

        # recording user details to records file
        with open('Records.csv', 'a', newline='') as pl:
            writer = csv.writer(pl)

            self.makeCard()

            # Finding Last ID
            def LastIDRecord():
                if os.path.getsize('Records.csv') == 0:
                    return 0
                else:
                    lastID = 0
                    with open('Records.csv', 'r') as re:
                        readfile = csv.reader(re)
                        for i in readfile:
                            if int(i[0]) > int(lastID):
                                lastID = i[0]
                        return int(lastID) + 1

            writer.writerow(
                [LastIDRecord(), self.getAccountType(),
                 self.getFullname(),
                 self.getaddress(),
                 self.getEmail(),
                 self.getPhoneNum(),
                 self.washCard.getCardNum(),
                 self.washCard.getBalance(),
                 self.washCard.getPoint()])

        messagebox.showerror("Success", "Account Created Successfully, Login Now")

    def login(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        with open('WebUser.csv', 'r') as re:
            readfile = csv.reader(re)
            for i in readfile:
                if i[1] == self.getUserName() and i[2] == self.getPassword():
                    self.setUserID(i[0])

        with open('Records.csv', 'r') as re:
            readfile = csv.reader(re)
            for i in readfile:
                if i[0] == self.getUserID():
                    self.setAccountType(i[1])
                    self.setFullname(i[2])
                    self.setAddress(i[3])
                    self.setEmail(i[4])
                    self.setPhoneNum(i[5])
                    card = WashCard()
                    self.setWashCard(card)
                    card.setBalance(float(i[7]))
                    card.setCardNum(i[6])
                    card.setPoint(int(i[8]))

    # Method to assign new washcard to new user
    def makeCard(self):
        cardN = self.generateCardNum()
        with open('Records.csv', 'r') as re:
            readfile = csv.reader(re)
            for i in readfile:
                if i[6] == cardN:
                    self.makeCard()
            washCard = WashCard()
            washCard.setCardNum(cardN)
            washCard.setBalance(0)
            if self.getAccountType() == 'Gold Member' or self.getAccountType() == 'Silver Member':
                washCard.setPoint(0)
            else:
                washCard.setPoint(-1)
            self.setWashCard(washCard)

    def generateCardNum(self):
        randAcc = random.randint(1000000000, 9999999999)
        cardnum = 'WSC' + str(randAcc)
        return cardnum

    # method to purchase a service
    def purchase(self, regWash, steamWash, detailing, touchless, selfWash):
        l = [regWash, steamWash, detailing, touchless, selfWash]
        for i in l:
            # if i == 'Regular Wash':
            if i == 'Regular Wash':
                wash = RegularWash()
                self.purchasedSerivces.append(wash)
            elif i == 'Steam Wash':
                wash = CarSteamWash()
                self.purchasedSerivces.append(wash)
            elif i == 'Detailing Wash':
                wash = CarDetailingWash()
                self.purchasedSerivces.append(wash)
            elif i == 'Touchless Wash':
                wash = CarTouchLessWash()
                self.purchasedSerivces.append(wash)
            elif i == 'self-wash':
                wash = SelfServiceWash()
                self.purchasedSerivces.append(wash)

    # method to return names of purchased services
    def namePuchasedService(self):
        l = []
        for i in self.getPurchasedService():
            l.append(i.getService())
        return l

    # method to calculate Total before discount
    def totalbeforeDiscount(self):
        total = 0
        for i in self.purchasedSerivces:
            total = total + i.getPrice()
        return total

    # method to calculate total after discount
    def totalAfterDiscount(self, dicount, total):
        if dicount != 0:
            messagebox.showerror("Congratulations", f"Congrat you got {dicount}% discount")
            return total - (total * (dicount / 100))
        else:
            return total

    # Topup method
    def topup(self, amt):
        found = 0
        m1 = []
        f = open('Records.csv', 'r')
        readfile = csv.reader(f)
        for i in readfile:
            if i[0] == self.getUserID():
                found = 1
                i[7] = amt + float(i[7])
                self.washCard.setBalance(amt + float(i[7]))
                if self.getAccountType() == 'Regular Member' and int(i[8]) == -1 and amt >= 100:
                    i[8] = -3
                    self.washCard.setPoint(-3)
            m1.append(i)
        with open('Records.csv', 'w', newline='') as re:
            writefile = csv.writer(re)
            writefile.writerows(m1)
        if found == 1:
            messagebox.showerror("Congratulations", f"You topup {amt} AED, Lets pay now")
        else:
            messagebox.showerror("Alert", "Opps Something went wrong, Please try again")

    # Payment method
    def pay(self):
        if float(self.washCard.getBalance()) >= int(
                self.totalAfterDiscount(self.discount(), self.totalbeforeDiscount())):
            m1 = []
            f = open('Records.csv', 'r')
            readfile = csv.reader(f)
            for i in readfile:
                if i[0] == self.getUserID():
                    i[7] = float(i[7]) - self.totalAfterDiscount(self.discount(), self.totalbeforeDiscount())
                    self.washCard.setBalance(
                        float(i[7]) - self.totalAfterDiscount(self.discount(), self.totalbeforeDiscount()))
                m1.append(i)
            with open('Records.csv', 'w', newline='') as re:
                writefile = csv.writer(re)
                writefile.writerows(m1)

            with open('products&prices', 'a', newline='') as re:
                writefile = csv.writer(re)
                for i in self.purchasedSerivces:
                    writefile.writerow([self.getUserID(), i.getPrice(), i.getService()])
            self.updatePoints()
            messagebox.showerror("Success", "Payment Success")
            messagebox.showerror("Thanks",
                                 "Thank You for buying our service, please use our washcard in our garages to accesses the purchased services, See you tFhere")
            quit()
        else:
            messagebox.showerror("Alert", "Don't have Enough Balance, Please Top up")

    # Method to update user Info
    def updateInfo(self, fullname, username, password, address, email, phone):
        m1 = []
        f = open('Records.csv', 'r')
        readfile = csv.reader(f)
        for i in readfile:
            if i[0] == self.getUserID():
                i[2] = fullname
                self.setFullname(fullname)
                i[3] = address
                self.setAddress(address)
                i[4] = email
                self.setEmail(email)
                i[5] = phone
                self.setPhoneNum(phone)
            m1.append(i)
        with open('Records.csv', 'w', newline='') as re:
            writefile = csv.writer(re)
            writefile.writerows(m1)

        m1 = []
        f = open('WebUser.csv', 'r')
        readfile = csv.reader(f)
        for i in readfile:
            if i[0] == self.getUserID():
                i[1] = username
                self.setUserName(username)
                i[2] = password
                self.setPassword(password)
            m1.append(i)
        with open('WebUser.csv', 'w', newline='') as re:
            writefile = csv.writer(re)
            writefile.writerows(m1)
        messagebox.showerror("Success", "Account Info Updated Successfully")

    # method to update points
    def updatePoints(self):
        if self.getAccountType() == 'Regular Member' and self.washCard.getPoint() == -3:
            self.washCard.setPoint(-2)
        elif self.getAccountType() == 'Gold Member' or self.getAccountType() == 'Silver Member':
            self.washCard.setPoint(self.washCard.getPoint() + self.totalbeforeDiscount())
        m1 = []
        f = open('Records.csv', 'r')
        readfile = csv.reader(f)
        for i in readfile:
            if i[0] == self.getUserID():
                i[8] = self.washCard.getPoint()
            m1.append(i)
        with open('Records.csv', 'w', newline='') as re:
            writefile = csv.writer(re)
            writefile.writerows(m1)

    # method to assign appropriate discount
    def discount(self):
        if self.getAccountType() == 'Regular Member':
            if self.washCard.getPoint() == -3:
                return 15
            else:
                return 0
        elif self.getAccountType() == 'Silver Member':
            if self.washCard.getPoint() >= 300:
                return 35
            else:
                return 0
        elif self.getAccountType() == 'Gold Member':
            if self.washCard.getPoint() >= 500:
                return 45
            else:
                return 0
        elif self.getAccountType() == 'Manager':
            return 50

        elif self.getAccountType() == 'Employee':
            return 30

    # method to assing view priviliage to manager
    def assingViewMan(self):
        if self.getAccountType() == 'Manager':
            m1 = []
            f = open('Records.csv', 'r')
            readfile = csv.reader(f)
            for i in readfile:
                m1.append(i)
            messagebox.showerror("Info", "Showing All Account types detail")
            return m1
        else:
            m1 = []
            f = open('Records.csv', 'r')
            readfile = csv.reader(f)
            for i in readfile:
                if i[1] != 'Manager' and i[1] != 'Employee':
                    m1.append(i)
            messagebox.showerror("Info", "Showing only user Account types detail")
            return m1

    def Delete(self):
        if self.getAccountType() == 'Manager':
            masbox= messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
            if masbox == 'yes':
                messagebox.showinfo("Info", "All accounts and passwords will be deleteted")
                with open('Records.csv', 'w', newline='') as re:
                    writefile = csv.writer(re)
                    writefile.writerows()
                with open('WebUser.csv', 'w', newline='') as re:
                    writefile = csv.writer(re)
                    writefile.writerows()
            else:
                messagebox.showinfo("Info", "Great Discision")
        else:
            messagebox.showinfo("Info", "Manager only can delete accounts")


class RegularUser(WebUser):
    '''Class to represent regular user of CleanCar.com'''

    # Initializer
    def __init__(self, userName='', password='', fullname='', address='', phone='', email=''):
        WebUser.__init__(self, userName, password, fullname, address, phone, email)


class Employee(WebUser):
    '''Class to represent employees of CleanCar.com'''

    # Initializer
    def __init__(self, userName='', password='', fullname='', address='', phone='', email=''):
        WebUser.__init__(self, userName, password, fullname, address, phone, email)


class RegularEmployee(Employee):
    '''Class to represent regular employees of CleanCar.com'''

    # Initializer
    def __init__(self, userName='', password='', fullname='', address='', phone='', email=''):
        Employee.__init__(self, userName, password, fullname, address, phone, email)


class Manager(Employee):
    '''Class to represent Manager of CleanCar.com'''

    # Initializer
    def __init__(self, userName='', password='', fullname='', address='', phone='', email=''):
        Employee.__init__(self, userName, password, fullname, address, phone, email)
