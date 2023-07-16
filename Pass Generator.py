#import & from
from tkinter import *
import pyperclip
import random
import logging

root = Tk("Password Generator")

root.geometry("900x900")  

root.wm_title("Password Generator")
root.adderrorinfo("Wait")

passstr = StringVar()

passlen = IntVar()


passlen.set(0)


def generate():

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password = ""

    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)


def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

Label(root, text="Enter password Length", font="50").pack(pady=3)

Entry(root, textvariable=passlen, font="50").pack(pady=3)


Button(root, text="Generate Password", command=generate, font="50").pack(pady=7)

Entry(root, textvariable=passstr, font="50").pack(pady=3)

Button(root, text="Copy Password", command=copytoclipboard, font="50").pack()

Label(root, text="\n\n\n\n\n\n\nMade By Ahmad_Carabit", font="bold 40").pack()

Label(root, text="\nMake Me Happy By Giving A Star ", font="bold 30").pack()

root.mainloop()