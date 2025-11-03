'''
MySQL Data Retrieval and CSV Export for Login Information

1. Connect to the MySQL database using the specified host, user, password, and database.
2. Create a cursor object to execute SQL queries.
3. Execute a SELECT query to fetch `s_no`, `de_date`, `email_id`, `user_name`, and `password` from the `login_information` table.
4. Fetch all rows returned by the query.
5. Extract the column names from the cursor description.
6. Convert the fetched rows into a pandas DataFrame for easy handling.
7. Use Tkinter's file dialog to allow the user to select a location and filename to save the CSV file.
8. If a file path is provided, export the DataFrame to CSV and print a success message.
9. If no file path is selected, print a cancellation message.
10. Close the database cursor and connection to free resources.
'''
import mysql.connector
import pandas as pd
import tkinter as tk
from tkinter import filedialog
connection = mysql.connector.connect(
    host='192.168.172.113',      
    user='User',       
    password='12345',  
    database='community_conversation'   
)
cursor = connection.cursor()
cursor.execute("SELECT s_no,de_date,email_id,user_name,password FROM login_information") 
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description]  
df = pd.DataFrame(rows, columns=columns)
root = tk.Tk()
root.withdraw()  
output_file_path = filedialog.asksaveasfilename(
    defaultextension=".csv", 
    filetypes=[("CSV files", "*.csv")],  
    title="Save CSV File"
)
if output_file_path:
    df.to_csv(output_file_path, index=False) 
    print(f"Data has been successfully exported to {output_file_path}")
else:
    print("No file was selected. The export was canceled.")
cursor.close()
connection.close()
