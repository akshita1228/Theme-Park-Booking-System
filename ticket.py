from tkinter import *   #Importing module for GUI
import sqlite3          #Importing module for Database connectivity
from tkinter import messagebox #Importing module for GUI Messagebox
import config              #Importing module containing global variables

conn=sqlite3.connect(('Theme Park.db')) #Creating db connection
c=conn.cursor() #Connection Variable


def cancel():
    can=messagebox.askyesno(25*" "+"Cancel Booking",message="Do you really want to Cancel Booking?")
    if(can==True):
        t.destroy()
        import theme_parks

def success():
    tickid=[]
    tickid.append(config.parkname[0:3])
    tickid.append(config.selloc[0:3])
    tickid.append(config.time)
    tickid.append(config.seattype[0:3])

    c.execute('SELECT phone_num FROM Customer WHERE cust_name="%s"'%config.customer)
    f=c.fetchall()
    o=f[0][0]

    tickid.append(o)

    c.execute('SELECT city_id FROM TpBranch WHERE branch_name="%s"'%config.bname)
    a=c.fetchall()
    h=a[0][0]

    ticketid="".join(map(str, tickid))
    c.execute('INSERT INTO Ticket(ticket_id, cust_id, park_name,city_id,timing,subtotal,tax,grandtotal,pts_used,noofticket) VALUES(?,?,?,?,?,?,?,?,?,?)'
              , (ticketid,o,config.parkname,h,config.time,config.subtotal,config.tax,config.gtotal,config.pts,config.quan))
    conn.commit()

    sss=str(ticketid[0:10])
    print(sss)
    seatid=sss
    gcap=20
    scap=80
    gprice=200
    sprice=100
    if(ticketid[10:13]=="GOL"):
        ch = c.execute('SELECT t_id FROM Express WHERE t_id ="%s"' % seatid)
        temp = ch.fetchall()
    elif(ticketid[10:13]=="SIL"):
        ch = c.execute('SELECT t_id FROM NonExpress WHERE t_id ="%s"' % seatid)
        temp = ch.fetchall()


    
    if len(temp) == 0:
        if(ticketid[10:13]=="GOL"):
            c.execute('INSERT INTO Express (t_id,capacity,price,availability) VALUES(?,?,?,?)'
                      , (seatid, gcap, gprice, gcap-config.quan))
            conn.commit()

            c.execute('INSERT INTO BranchExpress (city_id,t_id) VALUES (?,?)', (h,seatid))
            conn.commit()

        elif(ticketid[10:13]=="SIL"):
            c.execute('INSERT INTO NonExpress (t_id,capacity,price,availability) VALUES(?,?,?,?)'
                      , (seatid, scap, sprice, gcap-config.quan))
            conn.commit()

            c.execute('INSERT INTO BranchNonExpress (city_id,t_id) VALUES (?,?)'
                        ,(h,seatid))
            conn.commit()
    else:
        if(ticketid[10:13]=="GOL"):
            x = c.execute('SELECT availability FROM Express WHERE t_id = "%s"' % seatid)
            ava = x.fetchall()[0][0]
            ava = ava - config.quan
            data = (ava, seatid)
            c.execute("UPDATE  Express set availability = ? WHERE t_id =?", data)
            conn.commit()
        elif(ticketid[10:13]=="SIL"):
            x = c.execute('SELECT availability FROM NonExpress WHERE t_id = "%s"' % seatid)
            ava = x.fetchall()[0][0]
            ava = ava - config.quan
            data = (ava, seatid)
            c.execute("UPDATE NonExpress set availability = ? WHERE t_id =?", data)
            conn.commit()
        
        if(config.use==1):
            c.execute("UPDATE Customer set privilige_pts= ? WHERE cust_name=?",(0,config.customer))
            conn.commit()
        
    addpts=((config.gtotal*10)/100)+config.pts
    c.execute("UPDATE Customer set privilige_pts= ? WHERE cust_name=?",(addpts,config.customer))
    conn.commit()




    ssuc=messagebox.showinfo(25*" "+"Successs",message="You have Successfully Booked the ticket")
    t.destroy()
    import theme_parks


def ticket_display():
    tpark_name=config.parkname
    no_of_ticks=config.quan
    pno_of_ticks = str(no_of_ticks)
    location=config.selloc
    seat_type=config.seattype
    sub_total=0
    if(seat_type=='GOLD'):
        sub_total=200*no_of_ticks
    elif(seat_type=="SILVER"):
        sub_total=100*no_of_ticks
    else:
        pass
    config.subtotal=sub_total
    psub=str(sub_total)
    if(config.use==1):
        disc=config.pts
    elif(config.use==0):
        disc=0
    pdisc=str(disc)
    gst=(((sub_total-disc)*18)/100)
    config.tax=gst
    pgst=str(gst)
    price=gst+sub_total-disc
    config.gtotal=price
    pprice=str(price)
    L0=Label(t,text="Ticket",bg='white',fg='red',font=("bold",20))
    L0.place(x=450,y=10)
    L1=Label(t,text=tpark_name,bg='white',fg='red',font=("bold",17))
    L1.place(x=400,y=70)
    l3=Label(t,text='Location: '+location,compound=LEFT,bg='white',fg='red',font=("bold",14))
    l3.place(x=310,y=130)
    l10=Label(t,text='Branch: '+config.bname,compound=LEFT,bg='white',fg='red',font=("bold",14))
    l10.place(x=310,y=170)
    l11=Label(t,text='Timing: '+config.time+' hrs',compound=LEFT,bg='white',fg='red',font=("bold",14))
    l11.place(x=310,y=220)
    l2=Label(t,text='No of Tickets: '+pno_of_ticks,bg='white',fg='red',font=("bold",14))
    l2.place(x=310,y=270)
    l4=Label(t,text='Ticket type: '+seat_type,bg='white',fg='red',font=("bold",14))
    l4.place(x=310,y=320)
    l5=Label(t,text='SubTotal: Rs. '+psub,bg='white',fg='red',font=("bold",12))
    l5.place(x=550,y=130)
    l10=Label(t,text = '-',bg='white',fg='red',font=("bold",12))
    l10.place(x=600,y=170)
    l11=Label(t,text='Discount:Rs. '+pdisc,bg='white',fg='red',font=("bold",12))
    l11.place(x=560,y=210)
    l7=Label(t,text = '+',bg='white',fg='red',font=("bold",12))
    l7.place(x=600,y=250)
    l6=Label(t,text='GST(18%):Rs. '+pgst,bg='white',fg='red',font=("bold",12))
    l6.place(x=540,y=290)
    l9=Label(t,text='_________________',bg='white',fg='red',font=("bold",12))
    l9.place(x=530,y=320)
    l7=Label(t,text='Grand Total = Rs.'+pprice,bg='white',fg='red',font=("bold",12))
    l7.place(x=525,y=360)
    
    confirmb=Button(t,text="Confirm Booking",bg='white', fg='red',font=("bold", 15),command=success)
    confirmb.place(x=400, y=470)

    cancelb=Button(t,text="Cancel Booking",bg='white', fg='red',font=("bold", 8),command=cancel)
    cancelb.place(x=440, y=520)



t=Tk()

t.configure(bg='white',highlightbackground="black",highlightthickness=10)
t.geometry('1000x1000')
t.title("Ticket")

ticket_display()



t.mainloop()