# 🎓 School Admission System (SAS)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-FF6F00?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Platform-Desktop-333333?style=for-the-badge" alt="Desktop">
</p>

<h1 align="center">School Admission System</h1>

<p align="center">
  <strong>A Simple Desktop-Based Student Admission Management System</strong>
</p>

<p align="center">
  A Python Tkinter and MySQL application designed to manage
  student information, class details, and admission records
  through a structured desktop interface.
</p>

<p align="center">
  <strong>🎓 Student Management • 🏫 Class Management • 📝 Admission Management</strong>
</p>

---

## 📌 Overview

The **School Admission System (SAS)** is a desktop-based academic mini project developed using **Python Tkinter** and **MySQL**.

The system provides separate modules for managing:

- 👨‍🎓 Student information
- 🏫 Class information
- 📝 Student admissions
- 🧭 Application navigation

It stores application data in a structured MySQL database and provides a graphical interface for performing common admission-management operations.

---

## 🎯 Problem Statement

Managing student admissions manually can make it difficult to maintain student information, class details, admission numbers, and roll numbers in an organized manner.

The **School Admission System** provides a computerized solution that allows these records to be maintained through a desktop application connected to a MySQL database.

---

## 💡 Proposed Solution

The system follows a simple workflow:

```text
             ┌─────────────────────┐
             │     Main Menu       │
             └──────────┬──────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
 │   Student   │ │    Class    │ │  Admission   │
 │   Master    │ │   Master    │ │     Form     │
 └──────┬──────┘ └──────┬──────┘ └──────┬───────┘
        │               │               │
        └───────────────┼───────────────┘
                        ▼
               ┌─────────────────┐
               │  MySQL Database │
               └─────────────────┘
```

---

# ✨ Key Features

### 👨‍🎓 Student Management
- Store student personal information
- Automatic student number generation
- Store address and contact information
- Record birth date, age and gender
- Store admission number and other student details

### 🏫 Class Management
- Create and manage class records
- Store class capacity
- Store division information
- Maintain class fee details
- Automatic class number generation

### 📝 Admission Management
- Select students dynamically
- Select classes dynamically
- Assign admission numbers
- Generate roll numbers
- Store admission dates
- Add admission remarks

### 🖥️ Desktop GUI
- User-friendly Tkinter interface
- Structured forms
- Main menu navigation
- Form clearing after successful submission

### 🗄️ Database Management
- MySQL database integration
- Structured relational tables
- Separate master and transaction records
- Data stored persistently in the database

---

# 🧩 System Modules

| Module | Description |
|---|---|
| 👨‍🎓 **Student Master** | Stores student personal information |
| 🏫 **Class Master** | Stores class capacity, division and fees |
| 📝 **Admission Form** | Assigns students to classes |
| 🧭 **Main Menu** | Central navigation between modules |

---

# 🔄 Application Workflow

```text
Start Application
       │
       ▼
   Main Menu
       │
       ├──────────────► Student Master
       │                     │
       │                     ▼
       │               Save Student
       │                     │
       │                     ▼
       │               MySQL Database
       │
       ├──────────────► Class Master
       │                     │
       │                     ▼
       │                Save Class
       │                     │
       │                     ▼
       │               MySQL Database
       │
       └──────────────► Admission Form
                             │
                             ▼
                    Select Student + Class
                             │
                             ▼
                       Save Admission
                             │
                             ▼
                      MySQL Database
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python 3.10** | Application development |
| 🖥️ **Tkinter** | Desktop GUI |
| 🗄️ **MySQL / MariaDB** | Database management |
| 🔌 **mysql-connector-python** | Python–MySQL connectivity |
| 📅 **datetime** | Date-related operations |

---

# 🗃️ Database Structure

### Database

```text
sas
```

The system uses three main tables.

---

## 👨‍🎓 `studmast` — Student Master

| Field | Description |
|---|---|
| `sno` | Student Number |
| `sname` | Student Name |
| `sadd` | Address |
| `city` | City |
| `contact` | Contact Number |
| `bdate` | Birth Date |
| `age` | Age |
| `gender` | Gender |
| `adno` | Admission Number |
| `caste` | Caste |
| `ph` | Physical Handicap |

---

## 🏫 `classmast` — Class Master

| Field | Description |
|---|---|
| `clno` | Class Number |
| `clname` | Class Name |
| `capacity` | Class Capacity |
| `div` | Division |
| `cfees` | Class Fees |

---

## 📝 `admission` — Admission Records

| Field | Description |
|---|---|
| `adno` | Admission Number |
| `addate` | Admission Date |
| `sno` | Student Number |
| `clno` | Class Number |
| `rollno` | Roll Number |
| `remark` | Remark |

---

# 📦 Python Packages

```text
tkinter
mysql-connector-python
datetime
```

Install the MySQL connector with:

```bash
pip install mysql-connector-python
```

> `tkinter` and `datetime` are commonly included with Python installations.

---

# 🚀 Getting Started

## 1️⃣ Prerequisites

Make sure the following are installed:

- Python 3.10
- MySQL or MariaDB
- MySQL Connector for Python

---

## 2️⃣ Clone the Repository

```bash
git clone https://github.com/bhimratna/school-admission-system.git
cd school-admission-system
```

---

## 3️⃣ Install Dependency

```bash
pip install mysql-connector-python
```

---

## 4️⃣ Create Database

Open MySQL and create the database:

```sql
CREATE DATABASE sas;
```

Then configure the database connection in the Python source code according to your local MySQL credentials.

---

## 5️⃣ Run the Application

```bash
python main.py
```

> Replace `main.py` with the actual entry-point filename if your project uses a different file.

---

# 📸 Screenshots

Add your actual application screenshots here.

Recommended screenshots:

```text
📷 Main Menu
📷 Student Master
📷 Class Master
📷 Admission Form
📷 Database Records
```

Example:

```md
![Main Menu](screenshots/main-menu.png)

![Student Master](screenshots/student-master.png)

![Admission Form](screenshots/admission-form.png)
```

---

# 📂 Project Structure

A typical project structure can be organized as:

```text
School-Admission-System/
│
├── main.py
├── student.py
├── class.py
├── admission.py
├── database.py
│
├── screenshots/
│   ├── main-menu.png
│   ├── student-master.png
│   ├── class-master.png
│   └── admission-form.png
│
├── README.md
└── requirements.txt
```

> Update the filenames above to match your actual project structure.

---

# 🔐 Data Management

The application separates information into different database tables:

```text
Student Information
        │
        ▼
    studmast
        │
        │
Class Information
        │
        ▼
    classmast
        │
        │
        ▼
   admission
        │
        ▼
 Admission Records
```

This structure keeps student, class, and admission information organized.

---

# 🎓 Academic Purpose

This project was developed as an **academic mini project** to demonstrate practical implementation of:

- Python programming
- GUI development
- Database connectivity
- CRUD-style data management
- Relational database design
- Form-based application development
- MySQL integration

---

# 🔮 Future Improvements

Possible future enhancements include:

- 🔐 User authentication
- 📊 Student and admission dashboard
- 🔎 Search and filter functionality
- 🖨️ Admission receipt generation
- 📄 Student report generation
- 📈 Admission statistics
- 📱 Web-based version using Django
- 📧 Email notifications
- ☁️ Cloud database integration

---

# 👨‍💻 Author

**Bhimratna Sardar**  
B.Tech Computer Engineering

<p align="center">
  <a href="https://github.com/bhimratna">
    <img src="https://img.shields.io/badge/GitHub-Bhimratna-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>
