'''
MySQL Data Retrieval and CSV Export

1. Connect to the MySQL database using host, user, password, and database name.
2. Execute a SELECT query to get the `chat_row` and `text_message` columns from the table.
3. Fetch all rows and store them in a pandas DataFrame for easy handling.
4. Open a file dialog to choose where to save the CSV file.
5. Export the DataFrame to CSV so it can be used for data cleaning and analysis.
6. Close the database cursor and connection to free resources.
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
cursor.execute("SELECT chat_row,text_message FROM conversation_text") 
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
