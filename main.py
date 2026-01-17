from tkinter import *
import os

win = Tk()
win.title("School Admission System")
win.geometry("500x350")
win.configure(bg="#0d1117")

title_font = ('Segoe UI', 20, 'bold')
btn_font = ('Segoe UI', 12, 'bold')

# ---------------- FUNCTIONS ----------------
def open_student():
    os.system("python student.py")

def open_class():
    os.system("python classmaster.py")

def open_admission():
    os.system("python admission.py")

# ---------------- UI ----------------
Label(
    win,
    text="School Admission System",
    font=title_font,
    bg="#0d1117",
    fg="#00e5ff"
).pack(pady=30)

Button(
    win,
    text="Student Master",
    font=btn_font,
    width=20,
    bg="#00b0ff",
    fg="black",
    command=open_student
).pack(pady=10)

Button(
    win,
    text="Class Master",
    font=btn_font,
    width=20,
    bg="#00b0ff",
    fg="black",
    command=open_class
).pack(pady=10)

Button(
    win,
    text="Admission",
    font=btn_font,
    width=20,
    bg="#00b0ff",
    fg="black",
    command=open_admission
).pack(pady=10)

Button(
    win,
    text="Exit",
    font=btn_font,
    width=20,
    bg="#ff5252",
    fg="black",
    command=win.destroy
).pack(pady=20)

win.mainloop()
