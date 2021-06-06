from tkinter import *   #Importing module for GUI
import sqlite3          #Importing module for Database connectivity
from tkinter import messagebox #Importing module for GUI Messagebox
import config              #Importing module containing global variables

conn=sqlite3.connect(('Theme Park.db')) #Creating db connection
c=conn.cursor() #Connection Variable

def logout():
    outq=messagebox.askyesno(25*" "+"LOGOUT?",message="Do you really want to logout?")
    if(outq==True):
        seat.destroy()
        import login_dbms

def cancel():
    can=messagebox.askyesno(25*" "+"Cancel Booking",message="Do you really want to Cancel Booking?")
    if(can==True):
        seat.destroy()
        import theme_parks

def pts():
    custr=config.customer
    c.execute('SELECT privilige_pts FROM CUSTOMER WHERE CUST_NAME="%s"'%custr)
    z=c.fetchall()
    ptss=z[0][0]
    ppp=messagebox.showinfo(10*" "+"Privilige Points",message="You have %d points."%ptss)

def exit():
    can=messagebox.askyesno(40*" "+"EXIT",message="Do you really want to Close The Application & Exit?")
    if(can==True):
        seat.destroy()

def gotick(types,quant):
    quant=int(quant)
    config.seattype=types
    config.quan=quant

    custr=config.customer
    c.execute('SELECT privilige_pts FROM CUSTOMER WHERE CUST_NAME="%s"'%custr)
    z=c.fetchall()
    ptss=z[0][0]
    pkp=messagebox.askyesno(10*" "+"Privilige Points",message="You have %d points.\nWould you like to use them?"%ptss)
    config.pts=ptss
    if(pkp==True):
        config.use=1
    seat.destroy()
    import ticket


seat=Tk()
seat.title(200*" "+"TICKET SELECT")
seat.geometry('1500x800')
seat.configure(bg='white')

cust_name=config.customer


seating=PhotoImage(file="sarrange.png")
seatingr = seating.subsample(1, 1)
movpic1lab=Label(seat,image=seatingr)
movpic1lab.place(x=150,y=220)

noshow=Label(seat,text="TICKET SELECTION",bg='white',fg='red', font=("Roboto", 40, 'bold'))
noshow.place(x=550,y=60)

sselect=Label(seat,text="Please Select Type of Ticket",bg='white',fg='red', font=("bold", 25))
sselect.place(x=700,y=250)

v=StringVar()
r1=Radiobutton(seat,text="Gold",var=v,value="GOLD",bg='white',fg='red',font=("bold", 25))

#r1=Radiobutton(seat,text="GOLD",var=v,value=1,bg='black',fg='gold',font=("bold", 25))
r1.place(x=700,y=300)
#glabel=Label(seat,text="Only "+gavailability+" Gold seats left",bg='black',fg='red', font=("bold", 20))
#glabel.place(x=800,y=300)
r2=Radiobutton(seat,text="Silver",var=v,value="SILVER",bg='white',fg='red',font=("bold", 25))
#r2=Radiobutton(seat,text="SILVER",var=v,value=2,indicator=0,bg='black',fg='gold',font=("bold", 25))
r2.place(x=700,y=350)
#slabel=Label(seat,text="Only "+savailability+" Gold seats left",bg='black',fg='red', font=("bold", 20))
#slabel.place(x=800,y=350)

noselect=Label(seat,text="Please Select Number of Tickets",bg='white',fg='red', font=("bold", 25))
noselect.place(x=700,y=430)
nos=Entry(seat,bg='white',fg='red',font=("bold", 25))
nos.place(x=700,y=480)

#r1.deselect()
#r2.deselect()

b1=Button(seat, text="Continue", width=20, bg='white', fg='red',font=("bold", 20), command = lambda :gotick (v.get(),nos.get()) )
b1.place(x=600, y=670)

Button(seat,text="Points",bg='white',fg='red',font=("bold",10),command=pts).place(x=1250,y=5)
Button(seat,text="Log Out",bg='white',fg='red',font=("bold",10),command=logout).place(x=1300,y=5)
Button(seat,text="Cancel",bg='white',fg='red',font=("bold",10),command=cancel).place(x=1360,y=5)
Button(seat,text="Exit",bg='white',fg='red',font=("bold",10),command=exit).place(x=1415,y=5)

seat.mainloop()