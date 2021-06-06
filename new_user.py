from tkinter import *   #Importing module for GUI
import sqlite3          #Importing module for Database connectivity
from tkinter import messagebox #Importing module for GUI Messagebox
import config              #Importing module containing global variables

conn=sqlite3.connect(('Theme Park.db')) #Creating db connection
c=conn.cursor() #Connection Variable

def exit():
    can=messagebox.askyesno(40*" "+"EXIT",message="Do you really want to Close The Application & Exit?")
    if(can==True):
        newuser.destroy()


def neuse():
    newuser.destroy()
    import login_dbms
count=0
def signup():
    global fields,em,num,acc,pas,count
    if(count==0):
        print(count)    
        fields=Label(newuser,text='',bg='white',fg='red',font=('bold',10))
        em=Label(newuser,text='',bg='white',fg='red',font=('bold',10))
        num=Label(newuser,text='',bg='white',fg='red',font=('bold',10))
        pas=Label(newuser,text='',bg='white',fg='red',font=('bold',10))
        count+=1
    email = Id.get()
    phone = phno.get()
    cname = Fullname.get()
    cpass = password.get()
    crpass = repass.get()
    points = 0
    #fields=StringVar()
    if(len(email)==0 or len(phone)==0 or len(cname)==0 or len(cpass)==0 or len(crpass)==0):
        fields.config(text="Fields cannot be empty")
        fields.place(x=130,y=395)
    elif('@' not in email or '.com' not in email):
        fields.destroy()
        em.config(text="Invalid E-mail entered!")
        #em=Label(newuser,text='Invalid E-mail Entered',bg='black',fg='red',font=('bold',10))
        em.place(x=400,y=180)
    elif(len(phone)!=10):
        fields.destroy()
        em.destroy()
        phone=int(phone)
        num.config(text="Invalid number entered!")
        num.place(x=400,y=230)
    elif(cpass!=crpass):
        fields.destroy
        em.destroy()
        num.destroy() 
        pas.config(text="Invalid password entered!")
        pas.place(x=400,y=280)
    
 
    else:
            fields.destroy()
            num.destroy()
            em.destroy()
            pas.destroy()
            x=c.execute('SELECT phone_num FROM Customer WHERE phone_num = "%s"'%phone)
            temp1=x.fetchall()

            if len(temp1) !=0:
                #print("You already have an account. Proceed to log in")
                acc=Label(newuser,text='You already have an account. Proceed to log in',bg='white',fg='red',font=('bold',10))
                acc.place(x=130,y=385)

            else:
                
                c.execute('INSERT INTO Customer (email,phone_num,cust_name,password,privilige_pts) VALUES(?,?,?,?,?)',
                       (email,phone,cname,cpass,points))
                conn.commit()
                newuser.destroy()
                import login_dbms        


newuser = Tk()
newuser.geometry('750x500')
newuser.title(100*" "+"SignUp Page")
newuser.configure(bg='white')
Fullname = StringVar()
Id = StringVar()
phno = StringVar()
password = StringVar()
repass = StringVar()


label_0 = Label(newuser, text="SignUp", width=15,bg='white',fg='red', font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(newuser, text="FullName", width=15,bg='white',fg='red', font=("bold", 10))
label_1.place(x=70, y=130)
entry_1 = Entry(newuser, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(newuser, text="E-mail", width=15,bg='white',fg='red',  font=("bold", 10))
label_2.place(x=70, y=180)
entry_2 = Entry(newuser, textvar=Id)
entry_2.place(x=240, y=180)

label_3 = Label(newuser, text="Phone Number", width=15,bg='white',fg='red',  font=("bold", 10))
label_3.place(x=70, y=230)
entry_3 = Entry(newuser, textvar=phno)
entry_3.place(x=240, y=230)


label_4 = Label(newuser, text="Password", width=15,bg='white',fg='red',  font=("bold", 10))
label_4.place(x=70, y=280)
entry_4 = Entry(newuser,show='*', textvar=password)
entry_4.place(x=240, y=280)

label_5 = Label(newuser, text="Confirm Password",bg='white',fg='red',  font=("bold", 10))
label_5.place(x=70, y=330)
entry_5 = Entry(newuser,show='*', textvar=repass)
entry_5.place(x=240, y=330)


b1=Button(newuser,text=' Login ', bg='white', fg='red',font=("bold",12), command=neuse)
b1.place(x=360, y=5)
Button(newuser, text=' Confirm ', width=20, bg='white', fg='red', command=signup).place(x=180, y=430)
Button(newuser,text=" Exit ",bg='white',fg='red',font=("bold",12),command=exit).place(x=420,y=5)

newuser.mainloop()