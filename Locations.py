from tkinter import *
import sqlite3
from tkinter import messagebox
import config

conn=sqlite3.connect(('Theme Park.db'))
c=conn.cursor()

def callseat(locname,branname,timee,locbutton):

    print(locname)
    print(branname)
    print(timee)
    config.selloc=locname
    config.time=timee
    config.bname=branname
    loc.destroy()
    import seat

def logout():
    outq=messagebox.askyesno(25*" "+"LOGOUT?",message="Do you really want to logout?")
    if(outq==True):
        loc.destroy()
        import login_dbms

def cancel():
    can=messagebox.askyesno(25*" "+"Cancel Booking",message="Do you really want to Cancel Booking?")
    if(can==True):
        loc.destroy()
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
        loc.destroy()


loc=Tk()
loc.title(200*" "+"LOCATION SELECT")
loc.geometry('1500x800')
loc.configure(bg='white')



cust_name=config.customer


locaa=Label(loc,text="SELECT LOCATION AND TIME",bg='white',fg='red', font=("Roboto", 40, 'bold'))
locaa.place(x=400,y=60)

text = Text(loc, height=18, width=80,bg='white',fg='red',wrap=WORD,padx=10,pady=10,font=('bold',20))
scroll = Scrollbar(loc, command=text.yview)
text.configure(yscrollcommand=scroll.set)

y = c.execute('SELECT t.city_id,location,address,branch_name FROM TpCity t '
                  'JOIN ThemePark m ON t.tp_name = m.tp_name '
                  'JOIN TpBranch h ON h.city_id = t.city_id WHERE m.tp_name = "%s"'%config.parkname)
locas = y.fetchall()

x = c.execute('SELECT timing FROM TpCity t '
                  'JOIN ThemePark m ON t.tp_name = m.tp_name '
                  'JOIN TpBranch h ON h.city_id = t.city_id WHERE m.tp_name = "%s"'%config.parkname)
timings = x.fetchall()


locnamesss=[]
bnamesss=[]
for i in range(len(locas)):
    tt=locas[i][1]
    ttt=locas[i][3]
    locnamesss.append(tt)
    bnamesss.append(ttt)

b=[]
for i in range(len(locas)):
    butt=Button(loc, text=locas[i][1]+"\n"+locas[i][2]+"\n"+locas[i][3]+"\n"+timings[i][0]+" hrs", bg='white', fg='red',font=("bold", 20))
    butt.config(command= lambda t=locnamesss[i],e=bnamesss[i],tim=timings[i][0], butt = butt: callseat(t,e,tim,butt))
    b+=[butt]


for i in range(len(b)):
    text.window_create(END, window=b[i])

text.place(x=100,y=150)
scroll.pack(side=RIGHT,fill=Y)

Button(loc,text="Points",bg='white',fg='red',font=("bold",10),command=pts).place(x=1250,y=5)
Button(loc,text="Log Out",bg='white',fg='red',font=("bold",10),command=logout).place(x=1300,y=5)
Button(loc,text="Cancel",bg='white',fg='red',font=("bold",10),command=cancel).place(x=1360,y=5)
Button(loc,text="Exit",bg='white',fg='red',font=("bold",10),command=exit).place(x=1415,y=5)


loc.mainloop()