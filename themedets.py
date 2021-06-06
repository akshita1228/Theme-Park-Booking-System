from tkinter import *   #Importing module for GUI
import sqlite3          #Importing module for Database connectivity
from tkinter import messagebox #Importing module for GUI Messagebox
import config              #Importing module containing global variables

conn=sqlite3.connect(('Theme Park.db')) #Creating db connection
c=conn.cursor() #Connection Variable

def locations():
    parks.destroy()
    import Locations

def logout():
    outq=messagebox.askyesno(25*" "+"LOGOUT?",message="Do you really want to logout?")
    if(outq==True):
        parks.destroy()
        import login_dbms

def cancel():
    can=messagebox.askyesno(25*" "+"Cancel Booking",message="Do you really want to Cancel Booking?")
    if(can==True):
        parks.destroy()
        import theme_parks

def pts():
    custr=config.customer
    c.execute('SELECT privilige_pts FROM CUSTOMER WHERE CUST_NAME="%s"'%custr)
    z=c.fetchall()
    pts=z[0][0]
    can=messagebox.showinfo(10*" "+"Privilige Points",message="You have %d points"%pts)

def exit():
    can=messagebox.askyesno(40*" "+"EXIT",message="Do you really want to Close The Application & Exit?")
    if(can==True):
        parks.destroy()


parks=Tk()
parks.title(200*" "+"Park Details")
parks.geometry('1500x800')
parks.configure(bg='white')

noshow=Label(parks,text="Theme Park",bg='white',fg='red', font=("Roboto", 40, 'bold'))
noshow.place(x=550,y=60)

mmm=config.parkname

c.execute("SELECT food_status,eligibility,DESCRIPTION,ticket_type,IMAGE FROM ThemePark WHERE tp_name=?",(mmm,))
dets=c.fetchall()

bimage=dets[0][4]

with open('nowshowingimage.png','wb') as y2k:
    y2k.write(bimage)

parkpic1=PhotoImage(file="nowshowingimage.png")
photoimagek = parkpic1.subsample(1, 1)
ppic1lab=Label(parks,image=photoimagek)
ppic1lab.place(x=50,y=200)

m_name=config.parkname
ttype=dets[0][3]
foods=dets[0][0]
eligi=dets[0][1]
descr=dets[0][2]
mov_name1=Label(parks,text=m_name,bg='white',fg='red', font=("Roboto", 45, 'bold'))
mov_name1.place(x=600,y=150)
gen=Label(parks,text="Ticket Type: ",bg='white',fg='red', font=("bold", 25))
gen.place(x=1100,y=300)
m_gen=Label(parks,text=ttype,bg='white',fg='red', font=("bold", 25))
m_gen.place(x=1300,y=300)
dirc=Label(parks,text="Food Included(Y/N): ",bg='white',fg='red', font=("bold", 25))
dirc.place(x=1100,y=350)
m_dirc=Label(parks,text=foods,bg='white',fg='red', font=("bold", 25))
m_dirc.place(x=1400,y=350)
rat=Label(parks,text="Eligibilty: ",bg='white',fg='red', font=("bold", 25))
rat.place(x=1100,y=400)
m_rat=Label(parks,text=eligi,bg='white',fg='red', font=("bold", 25))
m_rat.place(x=1250,y=400)
descri=Label(parks,text="Description",bg='white',fg='red', font=("bold", 25))
descri.place(x=500,y=300)


text = Text(parks, height=8, width=35,bg='white',fg='red',wrap=WORD,padx=10,pady=10,font=('bold',20))
scroll = Scrollbar(parks, command=text.yview)
text.configure(yscrollcommand=scroll.set)
#text.window_create(END, window=m_descri)
text.insert(INSERT,descr)

text.place(x=500,y=350)
scroll.pack(side=RIGHT,fill=Y)

Button(parks, text="Continue", width=20, bg='white', fg='red',font=("bold", 20),command=locations).place(x=650, y=650)
Button(parks,text="Points",bg='white',fg='red',font=("bold",10),command=pts).place(x=1250,y=5)
Button(parks,text="Log Out",bg='white',fg='red',font=("bold",10),command=logout).place(x=1300,y=5)
Button(parks,text="Cancel",bg='white',fg='red',font=("bold",10),command=cancel).place(x=1360,y=5)
Button(parks,text="Exit",bg='white',fg='red',font=("bold",10),command=exit).place(x=1415,y=5)

parks.mainloop()
