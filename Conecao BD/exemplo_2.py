import mysql.connector #pip install mysql-connector-python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import bcrypt #pip install bcrypt

# Conectar ao banco de dados MySQL
def connect_db():
    global conn
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase" # Banco de dados mydatabase2
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    firstname VARCHAR(50) NOT NULL,
                    lastname VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    pass VARCHAR(255) NOT NULL,
                    birthdate DATE NOT NULL,
                    gender ENUM('male', 'female', 'other') NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    reset_token VARCHAR(100),
                    reset_token_expiration DATETIME)''')
    conn.commit()
    cursor.close()

# Função para criar o hash bcrypt da senha
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Inserir novo registro no banco de dados
def insert_record():
    cursor = conn.cursor()
    hashed_pass = hash_password(entry_pass.get())  # Hash da senha
    cursor.execute("INSERT INTO usuarios (firstname, lastname, email, pass, birthdate, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                   (entry_firstname.get(), entry_lastname.get(), entry_email.get(), hashed_pass,
                    entry_birthdate.get(), gender_var.get()))
    conn.commit()
    cursor.close()
    entry_firstname.delete(0, END)
    entry_lastname.delete(0, END)
    entry_email.delete(0, END)
    entry_pass.delete(0, END)
    entry_birthdate.delete(0, END)
    messagebox.showinfo("Success", "Record added successfully!")
    display_records()

# Visualizar registros do banco de dados
def display_records():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
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
    new_firstname = entry_firstname.get()
    new_lastname = entry_lastname.get()
    new_email = entry_email.get()
    new_pass = hash_password(entry_pass.get())  # Hash da nova senha
    new_birthdate = entry_birthdate.get()
    new_gender = gender_var.get()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET firstname=%s, lastname=%s, email=%s, pass=%s, birthdate=%s, gender=%s WHERE id=%s",
                   (new_firstname, new_lastname, new_email, new_pass, new_birthdate, new_gender, record_id))
    conn.commit()
    cursor.close()
    messagebox.showinfo("Success", "Record updated successfully!")
    display_records()

# Deletar registro selecionado
def delete_record():
    selected_item = listbox.selection()[0]
    record_id = listbox.item(selected_item, 'values')[0]
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (record_id,))
    conn.commit()
    cursor.close()
    messagebox.showinfo("Success", "Record deleted successfully!")
    display_records()

# Configurar a interface Tkinter
root = Tk()
root.title("Tkinter com Banco de Dados MySQL")
root.geometry("1920x768")

# Widgets de Entrada
Label(root, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
entry_firstname = Entry(root)
entry_firstname.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
entry_lastname = Entry(root)
entry_lastname.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = Entry(root)
entry_email.grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Password:").grid(row=3, column=0, padx=5, pady=5)
entry_pass = Entry(root, show="*")
entry_pass.grid(row=3, column=1, padx=5, pady=5)

Label(root, text="Birthdate:").grid(row=4, column=0, padx=5, pady=5)
entry_birthdate = Entry(root)
entry_birthdate.grid(row=4, column=1, padx=5, pady=5)

Label(root, text="Gender:").grid(row=5, column=0, padx=5, pady=5)
gender_var = StringVar(root)
gender_var.set("male")
gender_menu = OptionMenu(root, gender_var, "male", "female", "other")
gender_menu.grid(row=5, column=1, padx=5, pady=5)

Button(root, text="Add Record", command=insert_record).grid(row=6, column=0, columnspan=2, pady=10)
Button(root, text="Update Record", command=update_record).grid(row=7, column=0, columnspan=2, pady=5)
Button(root, text="Delete Record", command=delete_record).grid(row=8, column=0, columnspan=2, pady=5)

# Listbox para exibir os registros
cols = ('ID', 'First Name', 'Last Name', 'Email', 'Pass', 'Birthdate','Gender', 'Created At', 'Reset Token', 'Reset Token Expiration')
listbox = ttk.Treeview(root, columns=cols, show='headings')
# Ajuste o tamanho das colunas na Treeview
listbox.column('ID', width=50)
listbox.column('First Name', width=100)
listbox.column('Last Name', width=100)
listbox.column('Email', width=150)
listbox.column('Pass', width=50)
listbox.column('Birthdate', width=100)
listbox.column('Gender', width=80)
listbox.column('Created At', width=150)
listbox.column('Reset Token', width=150)
listbox.column('Reset Token Expiration', width=180)

for col in cols:
    listbox.heading(col, text=col)
listbox.grid(row=0, column= 2, rowspan=9, padx=10, pady=10, sticky='ns')


# Inicializar e exibir os registros existentes
connect_db()
display_records()

# Função para recarregar os registros do banco de dados e atualizar a exibição
def reload_records():
    connect_db()
    display_records()

# Botão para recarregar os registros
reload_button = Button(root, text="Reload", command=reload_records)
reload_button.grid(row=9, column=2, padx=5, pady=5)


# Iniciar o loop da aplicação Tkinter
root.mainloop()
