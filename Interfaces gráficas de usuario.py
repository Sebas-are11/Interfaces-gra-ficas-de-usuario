import tkinter as tk
from tkinter import messagebox

# Función para agregar el texto del campo a la lista
def agregar_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)  # Inserta el nuevo elemento al final de la lista
        entry.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista de elementos
def limpiar_lista():
    listbox.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")

# Etiqueta para el campo de texto
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto para ingresar datos
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Botón para agregar el dato a la lista
btn_agregar = tk.Button(root, text="Agregar", command=agregar_item)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Botón para limpiar la lista de datos
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Iniciar el loop principal de la GUI
root.mainloop()
