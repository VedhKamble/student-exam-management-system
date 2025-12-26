# db/database.py

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "",               # <-- user will configure
    "password": "",          # <-- user will configure
    "database": "exam_system"
}


def get_connection(use_database: bool = True):
    kwargs = {
        "host": DB_CONFIG["host"],
        "user": DB_CONFIG["user"],
        "password": DB_CONFIG["password"],
    }
    if use_database:
        kwargs["database"] = DB_CONFIG["database"]
    return mysql.connector.connect(**kwargs)


def initialize_database():
    try:
        # Connect without selecting a database so we can create it if missing
        conn = get_connection(use_database=False)
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        cursor.execute(f"USE {DB_CONFIG['database']}")

        # User table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(20) UNIQUE NOT NULL,
                password_hash VARCHAR(64) NOT NULL
            )
        """)

        # Student profile table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_profile (
                adm_no INT PRIMARY KEY,
                roll_no INT UNIQUE,
                name VARCHAR(50),
                mother_name VARCHAR(50),
                father_name VARCHAR(50),
                gender CHAR(1),
                class_name VARCHAR(5),
                section CHAR(1)
            )
        """)

        # Result table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                adm_no INT PRIMARY KEY,
                exam_name VARCHAR(30),
                sub1 INT,
                sub2 INT,
                sub3 INT,
                sub4 INT,
                sub5 INT,
                total INT,
                percentage FLOAT,
                attendance FLOAT,
                grade CHAR(1),
                remarks VARCHAR(100),
                FOREIGN KEY (adm_no) REFERENCES student_profile(adm_no)
            )
        """)

        conn.commit()
        conn.close()
        print("Database initialized successfully")

    except Error as e:
        print("Database error:", e)
