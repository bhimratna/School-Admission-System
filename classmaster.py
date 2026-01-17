from tkinter import *
from tkinter import messagebox
import mysql.connector

win = Tk()
win.title("Class Master")
win.geometry("600x400")
win.configure(bg="#0d1117")

f1=('Segoe UI',12,'bold')

def dbconn():
    return mysql.connector.connect(
        host="localhost",user="root",password="",database="sas"
    )

def clear():
    txtclname.delete(0,END)
    txtcap.delete(0,END)
    txtdiv.delete(0,END)
    txtfees.delete(0,END)

def maxrec():
    db=dbconn(); cur=db.cursor()
    cur.execute("SELECT MAX(clno) FROM classmast")
    r=cur.fetchone()
    clno = 1 if (not r) or (r[0] is None) else r[0] + 1
    txtclno.delete(0,END)
    txtclno.insert(0,str(clno))
    clear()

def save():
    try:
        db = dbconn()
        cur = db.cursor()

        cur.execute("""
            INSERT INTO classmast
            (clno, clname, capacity, division, cfees)
            VALUES (%s,%s,%s,%s,%s)
        """, (
            txtclno.get(),
            txtclname.get(),
            txtcap.get(),
            txtdiv.get(),
            txtfees.get()
        ))

        db.commit()   # 🔥 THIS WAS MISSING
        messagebox.showinfo("Success", "Class Saved Successfully")
        maxrec()

    except Exception as e:
        messagebox.showerror("Error", str(e))



Label(win,text="Class Master",font=('Segoe UI',20,'bold'),
      bg="#0d1117",fg="#00e5ff").pack(pady=20)

labels=["Class No","Class Name","Capacity","Division","Fees"]
for i,l in enumerate(labels):
    Label(win,text=l,font=f1,bg="#0d1117",fg="white").place(x=80,y=80+i*35)

txtclno=Entry(win,font=f1); txtclno.place(x=260,y=80)
txtclname=Entry(win,font=f1); txtclname.place(x=260,y=115)
txtcap=Entry(win,font=f1); txtcap.place(x=260,y=150)
txtdiv=Entry(win,font=f1); txtdiv.place(x=260,y=185)
txtfees=Entry(win,font=f1); txtfees.place(x=260,y=220)

Button(win,text="ADD",font=f1,command=maxrec).place(x=200,y=280)
Button(win,text="SAVE",font=f1,command=save).place(x=300,y=280)

maxrec()
win.mainloop()
