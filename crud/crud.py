import csv
import os


def initialize_csv():
    if not os.path.exists('record.csv'):
        with open('record.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Email"])

def add_record():
    id_ = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    email = input("Enter Email: ")
    
    with open('record.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_, name, age, email])
    print("Record added successfully!\n")

def display_records():
    with open('record.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def update_record():
    records = []
    id_ = input("Enter ID to update: ")
    found = False
    
    with open('record.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id_:
                name = input("Enter new Name: ")
                age = input("Enter new Age: ")
                email = input("Enter new Email: ")
                records.append([id_, name, age, email])
                found = True
            else:
                records.append(row)
    print(records)
    with open('record.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)
    
    if found:
        print("Record updated successfully!\n")
    else:
        print("Record not found!\n")

def delete_record():
    records = []
    id_ = input("Enter ID to delete: ")
    found = False
    
    with open('record.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != id_:
                records.append(row)
            else:
                found = True
    
    with open('record.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)
    
    if found:
        print("Record deleted successfully!\n")
    else:
        print("Record not found!\n")

def menu():
    initialize_csv()
    while True:
        print("\nCRUD Application")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_record()
        elif choice == '2':
            display_records()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            print("Exiting...\n")
            break
        else:
            print("Not a right  choice! Try again.\n")

menu()









# import sqlite3

# DB_NAME = "records.db"

# def initialize_db():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS records (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             age INTEGER,
#             email TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# def add_record():
#     id_ = input("Enter ID: ")
#     name = input("Enter Name: ")
#     age = input("Enter Age: ")
#     email = input("Enter Email: ")
    
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO records (id, name, age, email) VALUES (?, ?, ?, ?)", (id_, name, age, email))
#     conn.commit()
#     conn.close()
#     print("Record added successfully!\n")

# def display_records():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM records")
#     rows = cursor.fetchall()
#     conn.close()
#     for row in rows:
#         print(" | ".join(map(str, row)))

# def update_record():
#     id_ = input("Enter ID to update: ")
#     name = input("Enter new Name: ")
#     age = input("Enter new Age: ")
#     email = input("Enter new Email: ")
    
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("UPDATE records SET name = ?, age = ?, email = ? WHERE id = ?", (name, age, email, id_))
#     conn.commit()
#     conn.close()
#     print("Record updated successfully!\n")

# def delete_record():
#     id_ = input("Enter ID to delete: ")
    
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM records WHERE id = ?", (id_,))
#     conn.commit()
#     conn.close()
#     print("Record deleted successfully!\n")

# def menu():
#     initialize_db()
#     while True:
#         print("\nCRUD Application")
#         print("1. Add Record")
#         print("2. Display Records")
#         print("3. Update Record")
#         print("4. Delete Record")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == '1':
#             add_record()
#         elif choice == '2':
#             display_records()
#         elif choice == '3':
#             update_record()
#         elif choice == '4':
#             delete_record()
#         elif choice == '5':
#             print("Exiting...\n")
#             break
#         else:
#             print("Invalid choice! Try again.\n")

# if __name__ == "__main__":
#     menu()
