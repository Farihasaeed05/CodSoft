from tkinter import *
import pyperclip
import random

root = Tk()
root.title("Password Generator")
root.geometry("350x400")
root.minsize(300,400)
root.maxsize(750,630)
root.configure(bg='black')

passstr = StringVar()
passlen = IntVar()
passlen.set("")

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
    Label(root, text="Copied to Clipboard", bg="red").place(x=110,y=350)

Label(root, text='Password Generator',font=("Courier New",18,'bold'),bg="darkBlue", fg="black", relief="sunken",border=3, width=20, height=2).pack(pady=25)

Label(root, text='Enter Password Length',font=("Courier New",11,'bold'), fg="white", bg='black', relief="flat",border=1, height=1).pack(pady=1)

Entry(root, textvariable=passlen, width=32, bd=2, font=("Courier New",8,'bold')).place(x=56,y=140)

Button(root, text="Generate Password",font=("Courier New",12,'bold'), bg="green", fg='black', width=17, relief="sunken",border=3, command=generate).place(x=80,y=185)

Entry(root, textvariable=passstr,width=32, bd=2, font=("Courier New",8,'bold')).place(x=56,y=250)

Button(root, text="Copy", command=copytoclipboard, font=("Courier New",12,'bold'), bg="teal", fg='black', width=6, relief="sunken",border=3).place(x=130,y=300)

root.mainloop()