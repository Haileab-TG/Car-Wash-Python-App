# Program Name: CleanCar.com Test Module
# Author: Haileab Tesfamaryam Goitum
# Date of Creation:  5 DEC 2020


from CarWash_GUI import LoginPage
from CarWash_System import WebUser
from tkinter import *


# web users instance
webuser= WebUser()

# GUI instance
root= Tk()
loginpage= LoginPage(root, webuser)
root.mainloop()