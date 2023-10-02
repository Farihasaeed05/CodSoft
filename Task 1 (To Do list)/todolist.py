import tkinter
import tkinter.messagebox
from tkinter import *
todolist_root = Tk()
todolist_root.title("To Do List")
todolist_root.geometry("360x380")
todolist_root.minsize(300,300)
todolist_root.maxsize(750,630)
def addtask():
    task=entry_tasks.get()
    if task!="":
       lb_tasks.insert(tkinter.END, task)
       entry_tasks.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning", message="Please enter a task to add")

def deletetask():
    try:
        index=lb_tasks.curselection()[0]
        lb_tasks.delete(index)
    except:
        tkinter.messagebox.showwarning(title="Warning", message="Please select a task to delete")

def updatetask():
    try:
        index=lb_tasks.curselection()
        updated_task=entry_tasks.get()
        if updated_task:
            lb_tasks.delete(index)
            lb_tasks.insert(index,updated_task)
            entry_tasks.delete(0,tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning", message="Please enter an updated task")
    except:
        tkinter.messagebox.showwarning(title="Warning", message="Please select a task to update")

frame_tasks = tkinter.Frame(todolist_root)
frame_tasks.pack()

lb_tasks = tkinter.Listbox(frame_tasks, height=10, width=43)
lb_tasks.pack(side=tkinter.LEFT)

scroll_tasks = tkinter.Scrollbar(frame_tasks)
scroll_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb_tasks.config(yscrollcommand=scroll_tasks.set)
scroll_tasks.config(command=lb_tasks.yview)

entry_tasks = tkinter.Entry(todolist_root, width=37)
entry_tasks.pack(pady=7)

add_tasks = tkinter.Button(todolist_root, text="ADD TASK", font="TimesNewRoman 10", bg="lawn Green",height=2, width=17, command=addtask)
add_tasks.pack(pady=7)

delete_tasks = tkinter.Button(todolist_root, text="DELETE TASK", font="TimesNewRoman 10", bg="crimson",height=2, width=17, command=deletetask)
delete_tasks.pack(pady=7)

update_tasks = tkinter.Button(todolist_root, text="UPDATE TASK", font="TimesNewRoman 10", bg="rosyBrown",height=2, width=17, command=updatetask)
update_tasks.pack(pady=7)

todolist_root.mainloop()
