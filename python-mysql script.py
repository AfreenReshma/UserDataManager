import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = connection.cursor()

name = input("Enter your name: ")
email = input("Enter your email: ")
department = input("Enter your department: ")

insert_query = "INSERT INTO table name(name, email, department) VALUES (%s, %s, %s)"
values = (name, email, department)
cursor.execute(insert_query, values)

try:
    cursor.execute("SELECT * FROM table name")
    rows = cursor.fetchall()

    if rows:
        print("Fetched data from the table:")
        for row in rows:
            print(row)
    else:
        print("No data found.")
except mysql.connector.Error as err:
    print(f"Error fetching data: {err}")

connection.commit()
cursor.close()
connection.close()
