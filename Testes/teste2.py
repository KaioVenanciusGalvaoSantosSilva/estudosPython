import tkinter as tk

# Create a new tkinter window
window = tk.Tk()


# Create a listbox with a height of 4 and a width of 10
listbox = tk.Listbox(window, height=8, width=25)

# Add functions to the listbox
listbox.insert(tk.END, "Soma")
listbox.insert(tk.END, "Subtração")
listbox.insert(tk.END, "Multiplicação")
listbox.insert(tk.END, "Divisão")
listbox.insert(tk.END, "Potência")

# Pack the listbox to make it visible
listbox.pack()


# Create entry fields for each value
entry_a = tk.Entry(window, width=10)
entry_b = tk.Entry(window, width=10)

# Pack the entry fields to make them visible
entry_a.pack()
entry_b.pack()

# Define the functions
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b

def potencia(a, b):
    return a ** b

# Create a function to handle the selection event
def on_select(event):
    selected_function = listbox.get(listbox.curselection())

    a = float(entry_a.get())
    b = float(entry_b.get())

    if selected_function == "Soma":
        result = soma(a, b)
    elif selected_function == "Subtração":
        result = subtracao(a, b)
    elif selected_function == "Multiplicação":
        result = multiplicacao(a, b)
    elif selected_function == "Divisão":
        result = divisao(a, b)
    elif selected_function == "Potência":
        result = potencia(a, b) 

    print(f"O resultado da função {selected_function} é: {result}")

# Bind the selection event to the on_select function
listbox.bind("<<ListboxSelect>>", on_select)

# Start the tkinter event loop
window.mainloop()