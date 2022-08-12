from cgitb import text
from sys import flags
from tkinter import*
import tkinter.messagebox
pro=Tk()
pro.title('Restaurant bot')
width=500
height=500
screenwidth = pro.winfo_screenwidth()
screenheight = pro.winfo_screenheight()
x = int((screenwidth - width)/2)
y = int((screenheight - height)/2)
pro.geometry(f"{width}x{height}+{x}+{y}")
pro.resizable(False,False)
pro.iconbitmap('D:\AMR\python project\\restaurant\\restaurant.ico')
l1=Label(pro,text='الفاتورة',font=('courier',15,"bold"),bg='black',fg='white')
l1.pack(fill=X)
f1=Frame(pro,bd=2,bg='white')
f1.place(x=0,y=0)
scrol=Scrollbar(f1,orient=VERTICAL)
textarea=Text(f1,yscrollcommand=scrol.set)
scrol.pack(fill=Y,side=LEFT)
scrol.config(command=textarea.yview)
textarea.pack(fill=BOTH,expand=1)
f2=Frame(pro,bd=2,width=500,height=100,bg='#0B4C5F')
f2.place(x=1,y=400)
flag=TRUE
def submit():
    flag=False
    if flag==False:
        tkinter.messagebox.showinfo('System','Thanks')
        pro.destroy()
        import Home
def exit():
    pro.destroy()
    import Home
bt1=Button(f2,text='Submit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=submit)
bt1.place(x=10,y=30)
bt2=Button(f2,text='Edit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1)
bt2.place(x=180,y=30)
bt2=Button(f2,text='Exit',font=('courier',15,"bold"),bg='black',fg='white',width=10,height=1,command=exit)
bt2.place(x=350,y=30)

pro.mainloop()