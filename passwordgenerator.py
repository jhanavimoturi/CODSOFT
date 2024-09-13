from tkinter import *
import string
import random

def generator():
    passwordField.delete(0,END)
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters =string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=10

    password=random.sample(all,password_length)
    passwordField.insert( 0,password)

def login():
    username = input("enter your username")
    password = input("enter your password")

root = Tk()
root.geometry("200x200")
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')

passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10)


generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=24,bd=2,font=Font)
passwordField.grid(pady=5)

copyButton=Button(root,text='Copy',font=Font)
copyButton.grid(pady=5)

root.mainloop()
