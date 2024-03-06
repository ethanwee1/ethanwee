#GUI_p5
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
import csv

def get_tables():
    conn = sqlite3.connect('unittest.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    conn.close()
    return tables

def filter_data():
    selected_table = table_var.get()
    if not selected_table:
        return
    conn = sqlite3.connect('unittest.db')
    cursor = conn.cursor()
    conditions = []
    if entry1.get():
        conditions.append(f"(test_file LIKE '%{entry1.get()}%' OR test_file IS NULL)")
    if entry2.get():
        conditions.append(f"(test_class LIKE '%{entry2.get()}%' OR test_class IS NULL)")
    if entry3.get():
        conditions.append(f"(test_name LIKE '%{entry3.get()}%' OR test_name IS NULL)")
    if entry4.get():
        conditions.append(f"(skip_reason LIKE '%{entry4.get()}%' OR skip_reason IS NULL)")
    if entry5.get():
        conditions.append(f"(assignee LIKE '%{entry5.get()}%' OR assignee IS NULL)")
    if entry6.get():
        conditions.append(f"(comments LIKE '%{entry6.get()}%' OR comments IS NULL)")
    if entry7.get():
        conditions.append(f"(status_set1 LIKE '%{entry7.get()}%' OR status_set1 IS NULL)")
    if entry8.get():
        conditions.append(f"(message_set1 LIKE '%{entry8.get()}%' OR message_set1 IS NULL)")
    if entry9.get():
        conditions.append(f"(status_set2 LIKE '%{entry9.get()}%' OR status_set2 IS NULL)")
    if entry10.get():
        conditions.append(f"(message_set2 LIKE '%{entry10.get()}%' OR message_set2 IS NULL)")

    query = f"SELECT * FROM {selected_table}"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query)
    rows = cursor.fetchall()
    update_table(rows)
    row_count_label.config(text=f"Rows returned: {len(rows)}")
    conn.close()

def update_table(rows):
    for item in tree.get_children():
        tree.delete(item)
    for row in rows:
        tree.insert('', 'end', values=row)

def clear_results():
    for item in tree.get_children():
        tree.delete(item)
    row_count_label.config(text="Rows returned: 0")

def write_to_csv():
    rows = tree.get_children()
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["test_file", "test_class", "test_name", "skip_reason", "assignee", "comments", "status_set1", "message_set1", "status_set2", "message_set2"])
        for row in rows:
            csvwriter.writerow(tree.item(row)['values'])

root = tk.Tk()
root.title("SQL Database Filter")

# Dropdown menu for selecting a table
table_var = tk.StringVar()
table_choices = get_tables()
table_dropdown = tk.OptionMenu(root, table_var, *table_choices)
table_dropdown.pack()

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

clear_button = tk.Button(root, text="Clear Results", command=clear_results)
clear_button.pack()

export_button = tk.Button(root, text="Export to CSV", command=write_to_csv)
export_button.pack()

# Treeview for displaying data
tree = ttk.Treeview(root, columns=("test_file", "test_class", "test_name", "skip_reason", "assignee", "comments", "status_set1", "message_set1", "status_set2", "message_set2"), show="headings")
tree.heading('test_file', text='test_file')
tree.heading('test_class', text='test_class')
tree.heading('test_name', text='test_name')
tree.heading('skip_reason', text='skip_reason')
tree.heading('assignee', text='assignee')
tree.heading('comments', text='comments')
tree.heading('status_set1', text='status_set1')
tree.heading('message_set1', text='message_set1')
tree.heading('status_set2', text='status_set2')
tree.heading('message_set2', text='message_set2')
tree.pack()

# Label for displaying the number of rows returned
row_count_label = tk.Label(root, text="Rows returned: 0")
row_count_label.pack()

root.mainloop()
