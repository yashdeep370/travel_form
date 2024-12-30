from tkinter import *

root = Tk()
root.geometry("644x344")

def getvals():
    print("it works")



Label(root, text="welcome to harry travels", font = "comicsans 13 bold").grid(row=0,column=3)

name = Label(root,text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
contact = Label(root, text="contact")
mode = Label(root, text="payment mode")

# packing with grid
name.grid(row =1 ,column=2)
phone.grid(row =2 ,column=2)
gender.grid(row =3 ,column=2)
contact.grid(row =4 ,column=2)
mode.grid(row =5 ,column=2)

# variables
namval = StringVar()
phonval = StringVar()
genval = StringVar()
contactval = StringVar()
modval = StringVar()
foodserval = IntVar()

#entry for form
namentry = Entry(root,textvariable=namval)
phonentry = Entry(root,textvariable=phonval)
genentry = Entry(root,textvariable=genval)
contactentry = Entry(root,textvariable=contactval)
modentry = Entry(root,textvariable=modval)

# packing entries
namentry.grid(row=1,column=3)
phonentry.grid(row=2,column=3)
genentry.grid(row=3,column=3)
contactentry.grid(row=4,column=3)
modentry.grid(row=5,column=3)

# /checkbox
foodservice =  Checkbutton(text="want to prebook your meals?",variable=foodserval)
foodservice.grid(row=6,column=3)

# buttonand packing and assigning it command

Button(text="sumnit to agency", command=getvals).grid(row=7,column=3)


root.mainloop()