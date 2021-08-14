from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.configure(bg="black")

def quit():
    root.destroy()
    
def button_click(number):
    current=box.get()
    box.delete(0,END)
    box.insert(0,str(current) + str(number))

def button_clear():
    box.delete(0,END)
    
def button_add():
    first_number=box.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    box.delete(0,END)
    
def button_equal():
    second_number=box.get()
    box.delete(0,END)
    if math == "addition":
        box.insert(0,f_num + int(second_number))
    if math == "subtraction":
        box.insert(0,f_num - int(second_number))
    if math == "multiplication":
        box.insert(0,f_num * int(second_number))
    if math == "division":
        box.insert(0,f_num / int(second_number))
    
    
def button_subtract():
    first_number=box.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    box.delete(0,END)

def button_multiply():
    first_number=box.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    box.delete(0,END)

def button_divide():
    first_number=box.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    box.delete(0,END)

box=Entry(root,width=30,fg="white",bg="black",borderwidth=5)
box.grid(row=0,column=0,columnspan=3)

button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1),fg="white",bg="black")
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2),fg="white",bg="black")
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3),fg="white",bg="black")
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4),fg="white",bg="black")
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5),fg="white",bg="black")
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6),fg="white",bg="black")
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7),fg="white",bg="black")
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8),fg="white",bg="black")
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9),fg="white",bg="black")
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0),fg="white",bg="black")
button_add=Button(root,text="+",padx=39,pady=20,command=button_add,fg="white",bg="black")
button_equal=Button(root,text="=",padx=86,pady=20,command=button_equal,fg="white",bg="black")
button_clear=Button(root,text="clear",padx=75,pady=20,command=button_clear,fg="white",bg="black")
button_subtract=Button(root,text="-",padx=42,pady=20,command=button_subtract,fg="white",bg="black")
button_multiply=Button(root,text="*",padx=41,pady=20,command=button_multiply,fg="white",bg="black")
button_divide=Button(root,text="/",padx=42,pady=20,command=button_divide,fg="white",bg="black")

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)


quit_button=Button(root,text="quit",command=quit,fg="white",bg="black")
quit_button.grid(row=99,column=0)
footer=Label(root,text="smithmule",fg="white",bg="black")
footer.grid(row=99,column=1)
root.mainloop()