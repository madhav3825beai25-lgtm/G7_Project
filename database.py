import sqlite3

# Connect to database
conn = sqlite3.connect("students.db", check_same_thread=False)

# Create cursor
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()


# CREATE - Add student
def add_student(roll_no, name, age, course):
    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (roll_no, name, age, course)
    )
    conn.commit()


# READ - Display students
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


# UPDATE - Update student
def update_student(roll_no, name, age, course):
    cursor.execute(
        """UPDATE students
        SET name=?, age=?, course=?
        WHERE roll_no=?""",
        (name, age, course, roll_no)
    )
    conn.commit()


# DELETE - Delete student
def delete_student(roll_no):
    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll_no,)
    )
    conn.commit()


print("SQLite Database Connected Successfully!")