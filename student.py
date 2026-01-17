from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from datetime import date, datetime
from tkinter.simpledialog import askstring
import mysql.connector

win=Tk()
win.title("Student Entry Form")
win.geometry("850x720")
win.configure(bg="#0d1117")

f1 = ('Segoe UI', 12, 'bold')
f2 = ('Segoe UI', 11, 'bold')

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Dark.TCombobox",
    fieldbackground="#161b22",   # entry area
    background="#161b22",
    foreground="white",
    arrowcolor="white"
)

style.map(
    "Dark.TCombobox",
    fieldbackground=[("readonly", "#161b22")],
    foreground=[("readonly", "white")],
    background=[("readonly", "#161b22")]
)

# dropdown list
win.option_add("*TCombobox*Listbox.background", "#161b22")
win.option_add("*TCombobox*Listbox.foreground", "white")
win.option_add("*TCombobox*Listbox.selectBackground", "#00e5ff")
win.option_add("*TCombobox*Listbox.selectForeground", "black")


def clsfields():
    txtsname.delete(0,END)
    txtsadd.delete(0,END)
    txtcity.delete(0,END)
    txtcontact.delete(0,END)
    txtbdate.delete(0,END)
    txtage.delete(0,END)
    txtgender.delete(0,END)
    txtadno.delete(0,END)
    txtcaste.delete(0,END)
    txtphysical.delete(0,END)
        
def maxrec():
    mydb= mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="sas"
    )
    mycur=mydb.cursor()
    mx=0
    mycur.execute("select max(sno) from studmast")
    mydata=mycur.fetchone()
    if mydata is not None and mydata[0] is not None:
        mx=mydata[0]
        mx=mx+1
    else:
        mx=1
    txtsno.delete(0,END)
    txtsno.insert(0,str(mx))
    clsfields()
    
    
def calc_age(event=None):
    try:
        dob = datetime.strptime(txtbdate.get(), "%Y-%m-%d")
        today = date.today()
        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )
        txtage.delete(0, END)
        txtage.insert(0, str(age))
    except:
        txtage.delete(0, END)


    


def maxaddno():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="sas"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(adno) from studmast")
    mydata = mycur.fetchone()

    if mydata is None or mydata[0] is None:
        mx = 1
    else:
        mx = int(mydata[0]) + 1  

    txtadno.delete(0, END)
    txtadno.insert(0, str(mx))



def saverec():
    s1=txtsno.get()
    s2=txtsname.get()
    s3=txtsadd.get()
    s4=txtcity.get()
    s5=txtcontact.get()
    if not s5.isdigit() or len(s5) != 10:
       messagebox.showinfo("Warn", "Contact Number must be exactly 10 digits")
       return

    s6=txtbdate.get()
    s7=txtage.get()
    s8=txtgender.get()
    s9=txtadno.get()
    s10=txtcaste.get()
    s11=txtphysical.get()

    
    
    
    if s2=="":
        messagebox.showinfo("Warn","Please Enter Student Name")
        return
    if s3=="":
        messagebox.showinfo("Warn","Please Enter Student Address")
        return
    if s4=="":
        messagebox.showinfo("Warn","Please Enter the City")
        return
    if s5=="":
        messagebox.showinfo("Warn","Please Enter Contact No")
        return
    if s6=="":
        messagebox.showinfo("Warn","Please Enter Birth Date")
        return
    if s7=="":
        messagebox.showinfo("Warn","Please Enter Age")
        return
    if s8=="":
        messagebox.showinfo("Warn","Please Enter Gender")
        return
    if s9=="":
        messagebox.showinfo("Warn","Please Enter Admission No")
        return
    if s10=="":
        messagebox.showinfo("Warn","Please Enter Caste")
        return
    if s11=="":
        messagebox.showinfo("Warn","Please Enter Physical Handicap Status")
        return
    
    
    mydb= mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="sas"
    )
    mycur=mydb.cursor()
    mycur.execute("insert into studmast values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+s6+"','"+s7+"','"+s8+"','"+s9+"','"+s10+"','"+s11+"')")
    mydb.commit()
    messagebox.showinfo("Confirm","Record Saved Successfully")
    maxrec()
    
    
def serrec():
    txtsno.delete(0,END)
    clsfields()
    s1=askstring("Find","Enter Serach Student No")
    mydb= mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="sas"
    )
    mycur=mydb.cursor()
    if not s1:
        messagebox.showinfo("Warn","No Student No entered")
        return
    try:
        s1_int = int(s1)
    except (ValueError, TypeError):
        messagebox.showinfo("Warn","Invalid Student No")
        return
    mycur.execute("select * from studmast where sno=%s", (s1_int,))
    mydata=mycur.fetchone()
    if mydata is None:
        messagebox.showinfo("Warn","Record Not Found")
        return
    else:
        txtsno.insert(0,mydata[0])
        txtsname.insert(0,mydata[1])
        txtsadd.insert(0,mydata[2])
        txtcity.insert(0,mydata[3])
        txtcontact.insert(0,mydata[4])
        txtbdate.insert(0, "" if mydata[5] is None else str(mydata[5]))
        txtage.insert(0,str(mydata[6]))
        txtgender.insert(0,mydata[7])
        txtadno.insert(0,mydata[8])
        txtcaste.insert(0,mydata[9])
        txtphysical.insert(0,mydata[10])
                
def uprec():
    s1=txtsno.get()
    s2=txtsname.get()
    s3=txtsadd.get()
    s4=txtcity.get()
    s5=txtcontact.get()
    if not s5.isdigit() or len(s5) != 10:
        messagebox.showinfo("Warn", "Contact Number must be exactly 10 digits")
        return


    s6=txtbdate.get()
    s7=txtage.get()
    s8=txtgender.get()
    s9=txtadno.get()
    s10=txtcaste.get()
    s11=txtphysical.get()
    
    if s2=="":
        messagebox.showinfo("Warn","Please Enter Customer Name")
        return
    if s3=="":
        messagebox.showinfo("Warn","Please Enter Customer Address")
        return
    if s4=="":
        messagebox.showinfo("Warn","Please Enter the State")
        return
    if s5=="":
        messagebox.showinfo("Warn","Please Enter Contact No")
        return
    if s6=="":
        messagebox.showinfo("Warn","Please Enter Birth Date")
        return
    if s7=="":
        messagebox.showinfo("Warn","Please Enter Age")
        return
    if s8=="":
        messagebox.showinfo("Warn","Please Enter Gender")
        return
    
    if s10=="":
        messagebox.showinfo("Warn","Please Enter Caste")
        return
    if s11=="":
        messagebox.showinfo("Warn","Please Enter Physical Handicap Status")
        return
    
    
    mydb= mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="sas"
    )
    mycur=mydb.cursor()
    mycur.execute("update studmast set sname='"+s2+"',sadd='"+s3+"',city='"+s4+"',contact='"+s5+"',bdate='"+s6+"',age='"+s7+"',gender='"+s8+"',caste='"+s10+"',ph='"+s11+"' where sno="+s1)
    mydb.commit()
    messagebox.showinfo("Confirm","Record Updated Successfully")
    maxrec()
    maxaddno()
    
def delrec():
    s1=txtsno.get()
    mydb= mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="sas"
    )
    ans=messagebox.askyesnocancel("Confirm","Are you sure to delete this record?")
    if ans==1:
        mycur=mydb.cursor()
        mycur.execute("delete from studmast where sno="+s1)
        mydb.commit()
        messagebox.showinfo("Confirm","Record Deleted Successfully")
        maxrec()


win.configure(bg="Black")   

l1 = Label(win, text='Student Entry Form', font=('Segoe UI', 22, 'bold'), bg="#0d1117", fg="#00e5ff")
l1.place(x=250, y=20)

l2 = Label(win, text='Student No :', font=f1, bg="#0d1117", fg="#c9d1d9")
l2.place(x=80, y=90)
txtsno = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtsno.place(x=300, y=90, width=260, height=30)

l3 = Label(win, text='Student Name :', font=f1, bg="#0d1117", fg="#c9d1d9")
l3.place(x=80, y=135)
txtsname = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtsname.place(x=300, y=135, width=260, height=30)

l4 = Label(win, text='Contact No :', font=f1, bg="#0d1117", fg="#c9d1d9")
l4.place(x=80, y=180)
txtcontact = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtcontact.place(x=300, y=180, width=260, height=30)

l5 = Label(win, text='Date Of Birth :', font=f1, bg="#0d1117", fg="#c9d1d9")
l5.place(x=80, y=225)
txtbdate = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtbdate.place(x=300, y=225, width=260, height=30)
txtbdate.bind("<FocusOut>", calc_age)

l5 = Label(win, text='(YYYY-MM-DD)', font=('Segoe UI', 9, 'italic'),bg="#0d1117", fg="#8b949e")
l5.place(x=610, y=225)

l6 = Label(win, text='Age :', font=f1, bg="#0d1117", fg="#c9d1d9")
l6.place(x=80, y=270)
txtage = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtage.place(x=300, y=270, width=260, height=30)
txtbdate.bind("<FocusOut>", calc_age)
txtbdate.bind("<Return>", calc_age)
txtbdate.bind("<KeyRelease>", calc_age)


l7 = Label(win, text='Gender :', font=f1, bg="#0d1117", fg="#c9d1d9")
l7.place(x=80, y=315)
txtgender = Combobox(win, values=["Male","Female","Other"],state="readonly", font=f1 , style="Dark.TCombobox")
win.option_add("*TCombobox*Listbox.background", "#161b22")
win.option_add("*TCombobox*Listbox.foreground", "white")

txtgender.place(x=300, y=315, width=260, height=30)


l8 = Label(win, text='Caste :', font=f1, bg="#0d1117", fg="#c9d1d9")
l8.place(x=80, y=360)
txtcaste = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtcaste.place(x=300, y=360, width=260, height=30)


l9 = Label(win, text='Handicap :', font=f1, bg="#0d1117", fg="#c9d1d9")
l9.place(x=80, y=405)
txtphysical = Combobox(win, values=["Yes","No"],state="readonly", font=f1 , style="Dark.TCombobox")
win.option_add("*TCombobox*Listbox.background", "#161b22")
win.option_add("*TCombobox*Listbox.foreground", "white")

txtphysical.place(x=300, y=405, width=260, height=30)

l10 = Label(win, text='Address :', font=f1, bg="#0d1117", fg="#c9d1d9")
l10.place(x=80, y=450)
txtsadd = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtsadd.place(x=300, y=450, width=260, height=30)

l11 = Label(win, text='City :', font=f1, bg="#0d1117", fg="#c9d1d9")
l11.place(x=80, y=495)
txtcity = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtcity.place(x=300, y=495, width=260, height=30)

l12 = Label(win, text='Admission No :', font=f1, bg="#0d1117", fg="#c9d1d9")
l12.place(x=80, y=540)
txtadno = Entry(win, bd=0, font=f1, bg="#161b22", fg="white",insertbackground="white")
txtadno.place(x=300, y=540, width=260, height=30)

def add_button_action():
    maxrec()
    maxaddno()
    
    
    
    
def add_hover_glow(btn, normal_bg, glow_bg):
    btn.configure(bg=normal_bg)

    btn.bind("<Enter>", lambda e: btn.configure(bg=glow_bg))
    btn.bind("<Leave>", lambda e: btn.configure(bg=normal_bg))
    
def textbox_outline(entry):
    entry.configure(
        highlightthickness=1,
        highlightbackground="#30363d",   # normal outline
        highlightcolor="#00e5ff"         # focus glow
    )

    entry.bind("<FocusIn>", lambda e: entry.configure(
        highlightthickness=2
    ))

    entry.bind("<FocusOut>", lambda e: entry.configure(
        highlightthickness=1
    ))

textbox_outline(txtsno)
textbox_outline(txtsname)
textbox_outline(txtcontact)
textbox_outline(txtbdate)
textbox_outline(txtage)
textbox_outline(txtcaste)
textbox_outline(txtsadd)
textbox_outline(txtcity)
textbox_outline(txtadno)




butadd = Button(win, text='ADD', font=f2, fg='black', width=8,command=add_button_action)
butadd.place(x=7, y=590)
add_hover_glow(butadd,  "#00b0ff", "#69f0ae")

butsave = Button(win, text='SAVE', font=f2, fg='black', width=8,command=saverec)
butsave.place(x=115, y=590)
add_hover_glow(butsave, "#00b0ff", "#40c4ff")

butser = Button(win, text='SEARCH', font=f2, fg='black', width=8,command=serrec)
butser.place(x=223, y=590)
add_hover_glow(butser, "#00b0ff", "#40c4ff")

butupdate = Button(win, text='UPDATE', font=f2, fg='black', width=8,command=uprec)
butupdate.place(x=331, y=590)
add_hover_glow(butupdate, "#00b0ff", "#69f0ae")

butdel = Button(win, text='DELETE', font=f2, fg='black', width=8,command=delrec)
butdel.place(x=439, y=590)
add_hover_glow(butdel, "#00b0ff", "#ff8a80")

butexit = Button(win, text='EXIT', font=f2, fg='black', width=8,command=win.destroy)
butexit.place(x=570, y=590)
add_hover_glow(butexit, "#ff1744", "#ff5252")



win.mainloop()