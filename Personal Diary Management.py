import mysql.connector


# Connect to MySQL
def connect():
    return mysql.connector.connect(host="localhost",user="root",password="root",database="Personal_Diary_Management")


# Add a new record
def add_record():
    conn = connect()
    cursor = conn.cursor()
    name = input("Enter Name: ")
    contact = int(input("Enter Contact No: "))
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")
    marital_status = input("If married enter 'Y' for Yes, else 'N' for No: ").upper()
    if marital_status == "Y":
        anniversary = input("Enter Anniversary date (YYYY-MM-DD): ")
    else:
        anniversary = None
    query = "INSERT INTO Personal_Diary(Name, Contact_No, Address, Email, DOB, Anniversary) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(name, contact, address, email, dob, anniversary))
    conn.commit()
    conn.close()
    print("Record added successfully!")


# Update a record
def update_record():
    conn = connect()
    cursor = conn.cursor()
    contact = int(input("Enter Contact No of the person to update: "))
    print("\n1. Name")
    print("2. Address")
    print("3. Email")
    print("4. DOB")
    print("5. Anniversary")
    choice = int(input("Enter field number to update: "))
    fields = ["Name", "Address", "Email", "DOB", "Anniversary"]
    if 1 <= choice <= 5:
        field = fields[choice - 1]
        new_value = input("Enter new value for " + field + ": ")
        query = ("UPDATE Personal_Diary SET "+ field + " = %s WHERE Contact_No = %s")
        cursor.execute(query, (new_value, contact))
        conn.commit()
        print("Record updated successfully!")
    else:
        print("Invalid field choice!")
    conn.close()


# Delete a record
def delete_record():
    conn = connect()
    cursor = conn.cursor()
    contact = int(input("Enter Contact No to delete: "))
    query = "DELETE FROM Personal_Diary WHERE Contact_No = %s"
    cursor.execute(query, (contact,))
    conn.commit()
    conn.close()
    print("Record deleted successfully!")


# View all records
def view_records():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Personal_Diary"
    cursor.execute(query)
    records = cursor.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No records found.")
    conn.close()


# View birthdays
def Birthday():
    conn = connect()
    cursor = conn.cursor()
    month = int(input("Enter month number (01 to 12): "))
    if 1 <= month <= 12:
        query = "SELECT Name, Contact_No, DOB FROM Personal_Diary WHERE MONTH(DOB) = %s"
        cursor.execute(query, (month,))
        records = cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No birthdays found for this month.")
    else:
        print("Invalid choice!")
    conn.close()


# View anniversaries
def Anniversary():
    conn = connect()
    cursor = conn.cursor()
    month = int(input("Enter month number (01 to 12): "))
    if 1 <= month <= 12:
        query = "SELECT Name, Contact_No, Anniversary FROM Personal_Diary WHERE MONTH(Anniversary) = %s"
        cursor.execute(query, (month,))
        records = cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No anniversaries found for this month.")
    else:
        print("Invalid choice!")
    conn.close()


# Main menu
while True:
    print("\n===== PERSONAL DIARY MANAGEMENT SYSTEM =====")
    print("1. Add New Record")
    print("2. Update Record")
    print("3. Delete Record")
    print("4. View All Records")
    print("5. View Birthdays")
    print("6. View Anniversary")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_record()

    elif choice == 2:
        update_record()

    elif choice == 3:
        delete_record()

    elif choice == 4:
        view_records()

    elif choice == 5:
        Birthday()

    elif choice == 6:
        Anniversary()

    elif choice == 7:
        print("End of Program")
        break

    else:
        print("Enter a Valid Choice")
