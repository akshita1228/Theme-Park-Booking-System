from tkinter import *
import sqlite3
from tkinter import messagebox
import config

conn=sqlite3.connect(('Theme Park.db'))
c=conn.cursor()


def exit():
    can=messagebox.askyesno(40*" "+"EXIT",message="Do you really want to Close The Application & Exit?")
    if(can==True):
        t.destroy()


def new_user():
    t.destroy()
    import new_user


def log_in():

    p = phno.get()
    x = c.execute('SELECT password FROM Customer WHERE phone_num = "%s"' % p)
    temp = x.fetchall()
    if len(temp) == 0:
        Label(t,text="This account doesn't exist.\n Please check entered details or create new account",bg='red',fg='white',font=("Roboto", 8, 'bold')).place(x=30,y=100) #Error Label
    else:
        k=c.execute('SELECT CUST_NAME FROM Customer WHERE phone_num = "%s"' % p)
        temp2=k.fetchall()
        config.customer=temp2[0][0]
        passwd = password.get()
        if passwd == temp[0][0]:
            t.destroy()
            import theme_parks
        else:
            Label(t,text="Incorrect username or password",bg='red',fg='white',font=("bold", 8)).place(x=67,y=100) #When password is incorrect

t=Tk() #Instance of GUI
phno = StringVar()
password = StringVar()
t.title(10*" "+"Login Page") #GUI Title
t.configure(bg='red')
t.geometry('500x500')
L1=Label(t,text="Login",bg='red',fg='white',width=20, font=("bold", 20)) #Page Header
L1.place(x=90,y=150)
l2=Label(t,text='Phone Number',bg='red',fg='white',width=15, font=("Roboto", 9, 'bold')) #Entry Label
l2.place(x=70,y=200)
e2=Entry(t,textvar=phno)
e2.place(x=180,y=200)
l3=Label(t,text='Password',bg='red',fg='white',width=15, font=("Roboto", 9, 'bold')) #Entry Label
l3.place(x=70,y=240)
e3=Entry(t,show='*',textvar=password) #Showing password as '*' during input
e3.place(x=180,y=240)
butt1=Button(t,text='New User',bg='red',fg='white',font=("Roboto", 9, 'bold'), command=new_user)  #New User Command Button
butt1.place(x=120,y=280)
butt2=Button(t,text='Log In',bg='red',fg='white',font=("Roboto", 9, 'bold'), command=log_in) #Log In Command Button
butt2.place(x=250,y=280)

Button(t,text=" Exit ",bg='red',fg='white',font=("Roboto", 9, 'bold'),command=exit).place(x=450,y=450)

t.mainloop()
