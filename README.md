# 🎓 Student Examination Management System

A GUI-based Student Examination Management System developed using **Python, Tkinter, and MySQL**.  
The system allows secure user authentication and complete management of student profiles, exam results, report cards, and performance analysis.

---

## 🚀 Features

### 🔐 Authentication
- User Registration & Login
- Secure password hashing

### 👨‍🎓 Student Management
- Add student profile
- Edit student details (field-wise)
- Delete student records

### 📝 Examination Module
- Enter exam marks and attendance
- Automatic calculation of:
  - Total marks
  - Percentage
  - Grade
  - Remarks

### 📊 Report & Analysis
- Text-based Report Card generation
- Subject-wise performance graph using Matplotlib

---

## 🖥️ Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Database:** MySQL
- **Visualization:** Matplotlib

---
## 📁 Project Structure
student-exam-management-system/
│
├── app.py
│
├── auth/
│   ├── login.py
│   └── register.py
│
├── db/
│   └── database.py
│
├── gui/
│   ├── dashboard.py
│   ├── student_add.py
│   ├── student_edit.py
│   ├── student_delete.py
│   ├── result_add.py
│   ├── report_card.py
│   └── performance_graph.py
│
├── utils/
│   └── security.py
│
├── assets/
│   └── Exam.png
│
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/student-exam-management-system.git
cd student-exam-management-system
2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Configure MySQL

Edit db/database.py:

DB_CONFIG = {
    "host": "localhost",
    "user": "your_user_name",
    "password": "your_mysql_password",
    "database": "exam_system"
}


Ensure MySQL server is running.

4️⃣ Run the application
python app.py

📌 Future Enhancements

Role-based access (Admin / Teacher)

Export report cards as PDF

Improved UI styling

Student login portal

👨‍💻 Author

Vedh Kamble
Python | Tkinter | MySQL
## 📁 Project Structure

