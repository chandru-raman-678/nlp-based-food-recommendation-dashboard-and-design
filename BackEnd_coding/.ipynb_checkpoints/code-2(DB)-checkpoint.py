'''
MySQL Data Retrieval and CSV Export for BMI Data

1. Connect to the MySQL database using host, user, password, and database name.
2. Create a cursor to interact with the database.
3. Execute a SELECT query to fetch the `bmi_value` and `age` columns from the `bmi_data` table.
4. Fetch all the rows returned by the query.
5. Extract the column names from the cursor and create a pandas DataFrame for easy data handling.
6. Use a Tkinter file dialog to let the user choose where to save the CSV file.
7. If a file path is selected, export the DataFrame to a CSV file.
8. Print a success message with the saved file path.
9. If no file is selected, print a cancellation message.
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
cursor.execute("SELECT bmi_value,age FROM bmi_data")  
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
