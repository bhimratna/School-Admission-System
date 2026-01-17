from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date
import mysql.connector

win = Tk()
win.title("Admission Form")
win.geometry("650x420")
win.configure(bg="#0d1117")

f1=('Segoe UI',12,'bold')

def dbconn():
    return mysql.connector.connect(
        host="localhost",user="root",password="",database="sas"
    )

def max_adno():
    db=dbconn(); cur=db.cursor()
    cur.execute("SELECT MAX(adno) FROM admission")
    r=cur.fetchone()
    adno = 1 if (r is None or r[0] is None) else r[0] + 1
    txtadno.delete(0,END)
    txtadno.insert(0,str(adno))
    txtdate.delete(0,END)
    txtdate.insert(0,str(date.today()))

def load_students():
    db=dbconn(); cur=db.cursor()
    cur.execute("SELECT sno,sname FROM studmast")
    rows = cur.fetchall() or []
    cmbstudent['values']=[f"{r[0]} - {r[1]}" for r in rows]
def load_classes():
    db=dbconn(); cur=db.cursor()
    cur.execute("SELECT clno,clname FROM classmast")
    rows = cur.fetchall() or []
    cmbclass['values']=[f"{r[0]} - {r[1]}" for r in rows]

def save():
    db = dbconn()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO admission
        (adno, addate, sno, clno, rollno, remark)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        txtadno.get(),
        txtdate.get(),
        cmbstudent.get().split(" - ")[0],
        cmbclass.get().split(" - ")[0],
        txtroll.get(),
        txtremark.get()
    ))

    db.commit()
    messagebox.showinfo("Success", "Admission Done")

    max_adno()        # next admission number
    clear_fields()    # 🔥 clear form

def clear_fields():
    # clear student/class selection and text fields (adno/date are reset by max_adno)
    try:
        cmbstudent.set('')
    except Exception:
        pass
    try:
        cmbclass.set('')
    except Exception:
        pass
    txtroll.delete(0, END)
    txtremark.delete(0, END)
    # focus back to student for convenience
    try:
        cmbstudent.focus_set()
    except Exception:
        pass

Label(win,text="Admission Form",font=('Segoe UI',20,'bold'),
      bg="#0d1117",fg="#00e5ff").pack(pady=20)

labels=["Admission No","Date","Student","Class","Roll No","Remark"]
for i,l in enumerate(labels):
    Label(win,text=l,font=f1,bg="#0d1117",fg="white").place(x=80,y=80+i*35)

txtadno=Entry(win,font=f1); txtadno.place(x=300,y=80)
txtdate=Entry(win,font=f1); txtdate.place(x=300,y=115)
cmbstudent=Combobox(win,state="readonly",font=f1); cmbstudent.place(x=300,y=150)
cmbclass=Combobox(win,state="readonly",font=f1); cmbclass.place(x=300,y=185)
txtroll=Entry(win,font=f1); txtroll.place(x=300,y=220)
txtremark=Entry(win,font=f1); txtremark.place(x=300,y=255)

Button(win,text="SAVE",font=f1,command=save).place(x=300,y=320)

max_adno()
load_students()
load_classes()
win.mainloop()
