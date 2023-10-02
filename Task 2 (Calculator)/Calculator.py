from tkinter import *
calculator_root = Tk()
calculator_root.title("Calculator")
calculator_root.configure(bg='black')
calculator_root.geometry("340x430")
calculator_root.minsize(300,300)
calculator_root.maxsize(750,630)

equation = ""
def clear():
    global equation
    equation = ""
    result_box.config(text=equation)
def show(value):
    global equation
    equation +=value
    result_box.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "ERROR"
            equation = ""
    result_box.config(text=result)



result_box=Label(calculator_root, text="", font=("Arial Bold",38), bg='aliceblue')
result_box.pack(fill=X, ipadx=20, pady=30, padx=15)

btn_1=Button(calculator_root,text="C", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="dodgerBlue",command=lambda:clear()).place(x=18,y=130)
btn_2=Button(calculator_root,text="/", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("/")).place(x=95,y=130)
btn_3=Button(calculator_root,text="%", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("%")).place(x=173,y=130)
btn_4=Button(calculator_root,text="+", width=5, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="darkorange",command=lambda:show("+")).place(x=251,y=130)

btn_5=Button(calculator_root,text="7", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("7")).place(x=17,y=187)
btn_6=Button(calculator_root,text="8", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("8")).place(x=95,y=187)
btn_7=Button(calculator_root,text="9", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("9")).place(x=173,y=187)
btn_8=Button(calculator_root,text="x", width=5, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="darkorange",command=lambda:show("x")).place(x=251,y=187)

btn_9=Button(calculator_root,text="4", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("4")).place(x=17,y=244)
btn_10=Button(calculator_root,text="5", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("5")).place(x=95,y=244)
btn_11=Button(calculator_root,text="6", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("6")).place(x=173,y=244)
btn_12=Button(calculator_root,text="-", width=5, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="darkorange",command=lambda:show("-")).place(x=251,y=244)

btn_13=Button(calculator_root,text="1", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("1")).place(x=17,y=300)
btn_14=Button(calculator_root,text="2", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("2")).place(x=95,y=300)
btn_15=Button(calculator_root,text="3", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("3")).place(x=173,y=300)
btn_16=Button(calculator_root,text="=", width=5, height=3, relief="sunken",border=2, font=("arial",17), fg="white", bg="darkorange",command=lambda:calculate()).place(x=251,y=300)

btn_17=Button(calculator_root,text="0", width=10, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show("0")).place(x=17,y=355)
btn_18=Button(calculator_root,text=".", width=4, height=1, relief="sunken",border=2, font=("arial",17), fg="white", bg="gray",command=lambda:show(".")).place(x=173,y=355)


calculator_root.mainloop()