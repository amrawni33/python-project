from tkinter import*
yy=Tk()
yy.title('Restaurant bot')
yy.iconbitmap('D:\AMR\python project\\restaurant\\restaurant.ico')
width=500
height=450
screenwidth = yy.winfo_screenwidth()
screenheight = yy.winfo_screenheight()
x = int((screenwidth - width)/2)
y = int((screenheight - height)/2)
yy.geometry(f"{width}x{height}+{x}+{y}")
yy.resizable(False,False)
c1=Checkbutton(yy, text='Toast')
c1.place(x=10,y=20)
l1=Label(yy,text='20 LG')
l1.place(x=220,y=20)
sp1=Spinbox(yy,from_=0,to=100,width='10')
sp1.place(x=130,y=20)
c2=Checkbutton(yy, text='Red Sauce Pizza')
c2.place(x=10,y=50)
l2=Label(yy,text='20 LG')
l2.place(x=220,y=50)
sp2=Spinbox(yy,from_=0,to=100,width='10')
sp2.place(x=130,y=50)
c3=Checkbutton(yy, text='Baps')
c3.place(x=10,y=80)
l3=Label(yy,text='20 LG')
l3.place(x=220,y=80)
sp3=Spinbox(yy,from_=0,to=100,width='10')
sp3.place(x=130,y=80)
c4=Checkbutton(yy, text='Croissants')
c4.place(x=10,y=110)
l4=Label(yy,text='20 LG')
l4.place(x=220,y=110)
sp4=Spinbox(yy,from_=0,to=100,width='10')
sp4.place(x=130,y=110)
c5=Checkbutton(yy, text='Assorted Wraps')
c5.place(x=10,y=140)
l5=Label(yy,text='20 LG')
l5.place(x=220,y=140)
sp5=Spinbox(yy,from_=0,to=100,width='10')
sp5.place(x=130,y=140)
c6=Checkbutton(yy, text='Assorted Paninis')
c6.place(x=10,y=170)
l6=Label(yy,text='20 LG')
l6.place(x=220,y=170)
sp6=Spinbox(yy,from_=0,to=100,width='10')
sp6.place(x=130,y=170)
c7=Checkbutton(yy, text='Chicken Toasties')
c7.place(x=10,y=200)
l7=Label(yy,text='20 LG')
l7.place(x=220,y=200)
sp7=Spinbox(yy,from_=0,to=100,width='10')
sp7.place(x=130,y=200)
c8=Checkbutton(yy, text='Assorted Quiches')
c8.place(x=10,y=230)
l8=Label(yy,text='20 LG')
l8.place(x=220,y=230)
sp8=Spinbox(yy,from_=0,to=100,width='10')
sp8.place(x=130,y=230)
c9=Checkbutton(yy, text='Assorted Salads')
c9.place(x=10,y=260)
l9=Label(yy,text='20 LG')
l9.place(x=220,y=260)
sp9=Spinbox(yy,from_=0,to=100,width='10')
sp9.place(x=130,y=260)
c10=Checkbutton(yy, text='Greek Pizza')
c10.place(x=10,y=290)
l10=Label(yy,text='20 LG')
l10.place(x=220,y=290)
sp10=Spinbox(yy,from_=0,to=100,width='10')
sp10.place(x=130,y=290)
c11=Checkbutton(yy, text='SUPER MELTS')
c11.place(x=10,y=320)
l11=Label(yy,text='20 LG')
l11.place(x=220,y=320)
sp11=Spinbox(yy,from_=0,to=100,width='10')
sp11.place(x=130,y=320)
c12=Checkbutton(yy, text='Grilled Shrimp')
c12.place(x=10,y=350)
l12=Label(yy,text='20 LG')
l12.place(x=220,y=350)
sp12=Spinbox(yy,from_=0,to=100,width='10')
sp12.place(x=130,y=350)
c13=Checkbutton(yy, text='Greek Salad')
c13.place(x=10,y=380)
l13=Label(yy,text='20 LG')
l13.place(x=220,y=380)
sp13=Spinbox(yy,from_=0,to=100,width='10')
sp13.place(x=130,y=380)
c14=Checkbutton(yy, text='Fish Sandwich')
c14.place(x=10,y=410)
l14=Label(yy,text='20 LG')
l14.place(x=220,y=410)
sp14=Spinbox(yy,from_=0,to=100,width='10')
sp14.place(x=130,y=410)
def submit():
    yy.destroy
    import result
def back():
    yy.destroy()
    import f2
bt1=Button(yy,text='Back',font=('courier',15,'bold'),bg='whitesmoke',activebackground='green',command=back)
bt1.place(x=420,y=400)
bt2=Button(yy,text='Submit',font=('courier',15,'bold'),bg='whitesmoke',activebackground='green',command=submit)
bt2.place(x=320,y=400)
yy.mainloop()