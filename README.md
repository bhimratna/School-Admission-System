# 🎓 School Admission System (SAS)

The **School Admission System (SAS)** is a desktop-based mini project developed using **Python Tkinter** and **MySQL**.  
It helps to manage **student details, class details, and admission records** in a structured and efficient way.

---

## 👨‍💻 Developer
**Name:** Bhimratna Sardar  

---

## ✨ Project Highlights
- User-friendly GUI using **Tkinter**
- Modular design (Student, Class, Admission)
- Normalized database structure
- Automatic ID generation
- Dynamic dropdowns for Student & Class
- Data stored securely in MySQL
- Clear form after successful save
- Suitable for academic mini-project

---

##  Modules
- **Student Master** – Stores student personal information  
- **Class Master** – Stores class details like capacity and fees  
- **Admission Form** – Assigns students to classes  
- **Main Menu** – Central navigation for all modules  

---

##  Technologies Used
- **Python 3.10**
- **Tkinter** (GUI)
- **MySQL / MariaDB**
- **mysql-connector-python**

---

## DataBase Structure MYSQL
-Database Name: sas

🔹 Table: studmast (Student Master)
Field Name	Description
sno	Student Number 
sname	Student Name
sadd	Address
city	City
contact	Contact Number
bdate	Birth Date
age	Age
gender	Gender
adno	Admission Number
caste	Caste
ph	Physical Handicap

🔹 Table: classmast (Class Master)
Field Name	Description
clno	Class Number (Primary Key)
clname	Class Name
capacity	Class Capacity
div	Division
cfees	Class Fees

🔹 Table: admission (Admission)
Field Name	Description
adno	Admission Number 
addate	Admission Date
sno	Student Number 
clno	Class Number 
rollno	Roll Number
remark	Remark



## 📦 Python Packages Used
```bash
tkinter
mysql-connector-python
datetime


