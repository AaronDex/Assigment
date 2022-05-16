import math
from tkinter import *
root = Tk()
root.title("Tax Calculator")
root.geometry("500x500")
    
###This is to find the tax bracket
def tax():
    while True:
        try:
            gross_income = (float(myEntry1.get()))
            tax_bracket1,tax_bracket2,tax_bracket3,tax_bracket4,= 18200,45000,120000,180000,
            take_home = "take home pay is"
            if float(gross_income < tax_bracket1):
                print("You have to pay no tax")
            elif float(gross_income < tax_bracket2):
                print(math.floor((gross_income - tax_bracket1)*19 /100))
                print(take_home)
            elif float(gross_income < tax_bracket3):
                print(math.floor((gross_income - tax_bracket2)*32.5 /100+5092))
            elif float(gross_income < tax_bracket4):
                print(math.floor((gross_income - tax_bracket3)*37 /100+29467))
            elif float(gross_income > tax_bracket4):
                print(math.floor((gross_income - tax_bracket4)*45 /100+51667))
        except:
            print("oops")
            raise
        else:
            break

###Define Widgets
myLabel1 = Label(root,text="Please enter your gross income for this finnical year: ")
myLabel2 = Label(root,text="How Many Cases Assigned?",)
myLabel3 = Label(root,text="How Many Cases Closed?",)
myLabel4 = Label(root,text="Current KPI?")
###User Input
myEntry1 = Entry(root)
myButton1 = Button(root,text="Submit",command=tax)
###Placing Widgets
myLabel1.grid(row=1,column=2)
###Placing Entry
myEntry1.grid(row=2,column=2)
myButton1.grid(row=2,column=4)
asdasdasdasd
mainloop()