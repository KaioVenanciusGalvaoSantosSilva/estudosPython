#pip install mysql-connector-python

import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Conectar ao banco de dados MySQL
def connect_db():
    global conn
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="programacao" #crie o banco de dados
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    age INT)''')
    conn.commit()
    cursor.close()

# Inserir novo registro no banco de dados
def insert_record():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (name, age) VALUES (%s, %s)", (entry_name.get(), entry_age.get()))
    conn.commit()
    cursor.close()
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    messagebox.showinfo("Success", "Record added successfully!")
    display_records()

# Visualizar registros do banco de dados
def display_records():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    cursor.close()
    for row in listbox.get_children():
        listbox.delete(row)
    for row in rows:
        listbox.insert("", END, values=row)

# Atualizar registro selecionado
def update_record():
    selected_item = listbox.selection()[0]
    record_id = listbox.item(selected_item, 'values')[0]
    new_name = entry_name.get()
    new_age = entry_age.get()
    cursor = conn.cursor()
    cursor.execute("UPDATE records SET name=%s, age=%s WHERE id=%s", (new_name, new_age, record_id))
    conn.commit()
    cursor.close()
    messagebox.showinfo("Success", "Record updated successfully!")
    display_records()

# Deletar registro selecionado
def delete_record():
    selected_item = listbox.selection()[0]
    record_id = listbox.item(selected_item, 'values')[0]
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id=%s", (record_id,))
    conn.commit()
    cursor.close()
    messagebox.showinfo("Success", "Record deleted successfully!")
    display_records()

# Configurar a interface Tkinter
root = Tk()
root.title("Tkinter com Banco de Dados MySQL")
root.geometry("800x600")

# Widgets de Entrada
Label(root, text="Name:").pack(pady=5)
entry_name = Entry(root)
entry_name.pack(pady=5)

Label(root, text="Age:").pack(pady=5)
entry_age = Entry(root)
entry_age.pack(pady=5)

Button(root, text="Add Record", command=insert_record).pack(pady=5)
Button(root, text="Update Record", command=update_record).pack(pady=5)  # Adicionando o botão para atualizar o registro

# Listbox para exibir os registros
cols = ('ID', 'Name', 'Age')
listbox = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    listbox.heading(col, text=col)
listbox.pack(pady=20)

Button(root, text="Delete Record", command=delete_record).pack(pady=5)

# Inicializar e exibir os registros existentes
connect_db()
display_records()

# Iniciar o loop da aplicação Tkinter
root.mainloop()
