#GUI_p3
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

def filter_data():
    conn = sqlite3.connect('unittest.db')
    cursor = conn.cursor()
    # Construct the query with multiple filter conditions
    query = f"""SELECT * FROM two_skip_miss_sm86_xml_20230927 WHERE 
    (test_file LIKE '%{entry1.get()}%'  OR test_file IS NULL)
AND (test_class LIKE '%{entry2.get()}%' OR test_name IS NULL)
AND (test_name LIKE '%{entry3.get()}%'  OR test_name IS NULL)
AND (skip_reason LIKE '%{entry4.get()}%'  OR skip_reason IS NULL)
AND (assignee LIKE '%{entry5.get()}%'  OR assignee IS NULL)
AND (comments LIKE '%{entry6.get()}%' OR comments IS NULL)
AND (status_set1 LIKE '%{entry7.get()}%'  OR status_set1 IS NULL)
AND (message_set1 LIKE '%{entry8.get()}%'  OR message_set1 IS NULL)
AND (status_set2 LIKE '%{entry9.get()}%' OR status_set2 IS NULL)
AND (message_set2 LIKE '%{entry10.get()}%' OR message_set2 IS NULL)"""
    cursor.execute(query)
    rows = cursor.fetchall()
    update_table(rows)
    conn.close()

def update_table(rows):
    for row in rows:
        tree.insert('', 'end', values=row)
def clear_results():
    for item in tree.get_children():
        tree.delete(item)
root = tk.Tk()
root.title("SQL Database Filter")

# Create entry fields for each column you want to filter by
label1 = tk.Label(root, text="test_file")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="test_class")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
label3 = tk.Label(root, text="test_name")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()
label4 = tk.Label(root, text="skip_reason")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()
label5 = tk.Label(root, text="assignee")
label5.pack()
entry5 = tk.Entry(root)
entry5.pack()
label6 = tk.Label(root, text="comments")
label6.pack()
entry6 = tk.Entry(root)
entry6.pack()
label7 = tk.Label(root, text="status_set1")
label7.pack()
entry7 = tk.Entry(root)
entry7.pack()
label8 = tk.Label(root, text="message_set1")
label8.pack()
entry8 = tk.Entry(root)
entry8.pack()
label9 = tk.Label(root, text="status_set2")
label9.pack()
entry9 = tk.Entry(root)
entry9.pack()
label10 = tk.Label(root, text="message_set2")
label10.pack()
entry10 = tk.Entry(root)
entry10.pack()


search_button = tk.Button(root, text="Search", command=filter_data)
search_button.pack()

clear_button = tk.Button(root, text="Clear Results", command= clear_results)
clear_button.pack()

# Assuming your_table has 2 columns, adjust the number of columns if needed
tree = ttk.Treeview(root, columns=("test_file","test_class",'test_name', 'skip_reason','assignee','comments','status_set1',"message_set1","status_set2","message_set2"),show = "headings")
tree.heading('test_file', text='test_file') 
tree.heading('test_class', text='test_class') 
tree.heading('test_name', text='test_name')  # Adjust the column name
tree.heading('skip_reason', text='skip_reason') 
tree.heading('assignee', text='assignee') 
tree.heading('comments', text='comments') 
tree.heading('status_set1', text='status_set1') 
tree.heading('message_set1', text='message_set1') 
tree.heading('status_set2', text='status_set2') 
tree.heading('message_set2', text='message_set2') 

tree.pack()

root.mainloop()
