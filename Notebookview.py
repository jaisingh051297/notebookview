from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("800x480")

my_note=ttk.Notebook()
my_note.pack()

Tool_1=Frame(my_note,width=800,height=480,bg="green")
Tool_2=Frame(my_note,width=800,height=480,bg="pink")
System_1=Frame(my_note,width=800,height=480,bg="blue")


Tool_1.pack(fill="both",expand=1)
Tool_2.pack(fill="both",expand=1)
System_1.pack(fill="both",expand=1)


my_note.add(Tool_1,text="Tool__1")
my_note.add(Tool_2,text="Tool__2")
my_note.add(System_1,text="System__1")


root.mainloop()