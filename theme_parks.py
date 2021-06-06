from tkinter import *   #Importing module for GUI
import sqlite3          #Importing module for Database connectivity
from tkinter import messagebox #Importing module for GUI Messagebox
import config              #Importing module containing global variables

conn=sqlite3.connect(('Theme Park.db')) #Creating db connection
c=conn.cursor() #Connection Variable


def parkk(name,butt): #Command Function
    config.parkname=name #Updating Global Variable as Movie name
    nowshowing.destroy() #Destroy Current Now Showing Page
    import themedets #Invoke Theme Description Page

def logout():
    outq=messagebox.askyesno(25*" "+"LOGOUT?",message="Do you really want to logout?")
    if(outq==True):
        nowshowing.destroy()
        import login_dbms

def pts():
    custr=config.customer
    c.execute('SELECT privilige_pts FROM CUSTOMER WHERE CUST_NAME="%s"'%custr)
    z=c.fetchall()
    pts=z[0][0]
    can=messagebox.showinfo(10*" "+"Privilige Points",message="You have %d points"%pts)

def exit():
    can=messagebox.askyesno(40*" "+"EXIT",message="Do you really want to Close The Application & Exit?")
    if(can==True):
        nowshowing.destroy()

nowshowing=Tk()
nowshowing.title(200*" "+"Theme Parks")
nowshowing.geometry('1500x800')
nowshowing.configure(bg='white')

cust_name=config.customer


noshow=Label(nowshowing,text="Theme Parks",bg='white',fg='red', font=("Roboto", 30, 'bold'))
noshow.place(x=500,y=60)

text = Text(nowshowing, height=35, width=150,bg='white')
scroll = Scrollbar(nowshowing, command=text.yview)
text.configure(yscrollcommand=scroll.set)

c.execute('SELECT tp_name,IMAGE FROM ThemePark')
f=c.fetchall()
namesss=[]
for i in range(len(f)):
    tt=f[i][0]
    namesss.append(tt)

b=[] #List to  store Buttons
img=[] #List to store Images
imgr=[] # List to store resized images


for i in range(len(f)): #For Loop to store images
    s=str(i)
    with open('see'+s+'.png','wb') as ddd: #New File for Image Created
        ddd.write(f[i][1]) #Wrote image in that fifle

    # Creating a photoimage object to use image 
    photok = PhotoImage(file = "see"+s+'.png') 
    img+=[photok] #Add image to image list
    
    # Resizing image to fit on button 
    photoimagek = photok.subsample(2, 2)
    imgr+=[photoimagek] #Add resized image to resized image list

    butt=Button(nowshowing, text=namesss[i],image=photoimagek,compound=TOP,bg='white', fg='red',font=("bold", 20))
    butt.config(command= lambda t=namesss[i], butt = butt: parkk(t, butt))

    b+=[butt] #Adding Button to button List

 

for i in range(len(b)):
    text.window_create(END, window=b[i]) #Placing Buttons on text field


text.place(x=100,y=150)
scroll.pack(side=RIGHT,fill=Y)


Button(nowshowing,text="Points",bg='white',fg='red',font=("bold",12),command=pts).place(x=1280,y=5)
Button(nowshowing,text="Log Out",bg='white',fg='red',font=("bold",12),command=logout).place(x=1340,y=5)
Button(nowshowing,text="Exit",bg='white',fg='red',font=("bold",12),command=exit).place(x=1410,y=5)


nowshowing.mainloop()