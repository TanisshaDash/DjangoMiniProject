# importing required library
import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    passwd="newpassword",  # your MySQL password
    database="mydb"        # your database name
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# 1️⃣ Create table if not exists
studentRecord = """
CREATE TABLE IF NOT EXISTS STUDENT ( 
    NAME VARCHAR(20) NOT NULL, 
    BRANCH VARCHAR(50), 
    ROLL INT NOT NULL,
    SECTION VARCHAR(5), 
    AGE INT
)
"""
cursorObject.execute(studentRecord)
print("Table created or already exists.")

# 2️⃣ Insert sample records
insert_query = """
INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)
VALUES (%s, %s, %s, %s, %s)
"""

students = [
    ("Alice", "CSE", 101, "A", 20),
    ("Bob", "ECE", 102, "B", 21),
    ("Charlie", "ME", 103, "A", 22)
]

# Use executemany to insert multiple rows at once
cursorObject.executemany(insert_query, students)
dataBase.commit()
print(f"{cursorObject.rowcount} records inserted successfully!")

# 3️⃣ Show all tables
cursorObject.execute("SHOW TABLES;")
tables = cursorObject.fetchall()
print("\nTables present in the database:")
for table in tables:
    print(f"- {table[0]}")

# 4️⃣ Fetch and display all records from STUDENT
cursorObject.execute("SELECT * FROM STUDENT;")
records = cursorObject.fetchall()
print("\nRecords in STUDENT table:")
for record in records:
    print(record)

# Disconnecting from the server
dataBase.close()
