# User Data Manager

## Project Description
User Data Manager is a Python and SQL-based project designed to manage user data efficiently. This application allows you to store, retrieve, update, and delete user information in a SQL database, providing a simple interface for data handling.

## Features
- **Add User**: Insert new user records with details like name, email, and department.
- **Retrieve User Data**: Query the database to retrieve user information.
- **Update User Data**: Modify existing user records.
- **Delete User**: Remove user data from the database.

## Technologies Used
- **Python**: For scripting the functionality.
- **SQL (MySQL)**: To manage and store user data.
- **MySQL Workbench**: As the database management tool.

## Setup Instructions
1. Clone the repository or download the files.
2. Install Python and MySQL if not already installed.
3. Set up the database by running the SQL script included in the `setup.sql` file.
4. Run `user_data_manager.py` to start managing user data.

## Usage
1. Run the Python script by executing the following code to connect with the database:
```sql
import mysql.connector
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = connection.cursor()


connection.commit()
cursor.close()
connection.close()
```

##Conclusion

The User Data Manager provides a straightforward and efficient way to manage user data with Python and SQL. This project highlights the power of integrating Python with a SQL database to perform essential CRUD (Create, Read, Update, Delete) operations. It can be expanded with additional features like user authentication, data validation, and error handling to create a more robust data management system. Whether for learning purposes or as a foundation for more advanced applications, the User Data Manager is a valuable tool for understanding database management with Python
