class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.classes = []

    def enroll(self, class_id):
        if len(self.classes) < 3:
            self.classes.append(class_id)
        else:
            print("Student already enrolled in 3 classes.")

class Class:
    def __init__(self, class_id):
        self.class_id = class_id
        self.students = []

    def add_student(self, student_id):
        self.students.append(student_id)

# Create 5 classes
classes = [Class(class_id) for class_id in range(1, 6)]

# Create 20 students
students = [Student(student_id) for student_id in range(1, 21)]

# Enroll each student in 1 to 3 classes
import random
for student in students:
    num_classes = random.randint(1, 3)
    classes_to_enroll = random.sample(range(1, 6), num_classes)
    for class_id in classes_to_enroll:
        student.enroll(class_id)
        classes[class_id - 1].add_student(student.student_id)

# Print enrollment information
for student in students:
    print(f"Student {student.student_id} is enrolled in classes: {student.classes}")

for class_obj in classes:
    print(f"Class {class_obj.class_id} has students: {class_obj.students}")
# add SQLite 
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Add data to the table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    student_name TEXT,
                    class_id INTEGER
                )''')

# Read data from the tabel
students = [
    (1, 'Alice', 1),
    (2, 'Bob', 2),
    (3, 'niko', 1),
    (4,'kian',3),
    (5,'lili',2),
    (6,'juli',2),
    (7,'sara',1),
    (8,'yara',3),
    (9, 'poneh', 3),
    (10, 'ali', 2),
    (11, 'hasti', 1),
    (12, 'violet', 2),
    (13, 'fiona', 1),
    (14, 'ilia', 3),
    (15, 'dara', 2),
    (16, 'kimia', 3),
    (17, 'amir', 1),
    (18, 'sam', 3),
    (19, 'tara', 2),
    (20, 'Bob', 1),
    # continue with more data
]


# Read data from the table
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# save changes and close the connection
conn.commit()
conn.close()
