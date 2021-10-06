from time import strftime
from tkinter import Label,Tk

tk = Tk()
tk.title("Clock")
tk.geometry("198x50")
tk.resizable(False,False)

clock_label = Label(tk, bg="blue",fg="white",font = ("Courier",30,'bold'),relief='flat')
clock_label.pack()

def update_label():
    current_time = strftime('%H:%M:%S')
    clock_label.configure(text = current_time)
    clock_label.after(80,update_label)
    
update_label()
tk.mainloop()
