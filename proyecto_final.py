import tkinter as tk
from tkinter import ttk, messagebox
import json

# ---------- Configuración ----------
ARCHIVO_DATOS = "inventario.json"
inventario = {}

# ---------- Funciones de persistencia ----------
def guardar_inventario():
    ordenado = dict(sorted(inventario.items()))
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(ordenado, archivo, indent=4)

def cargar_inventario():
    global inventario
    try:
        with open(ARCHIVO_DATOS, "r") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = {}

# ---------- Funciones de gestión ----------
def agregar_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    try:
        cantidad = int(entrada_cantidad.get())
        if fruta:
            inventario[fruta] = inventario.get(fruta, 0) + cantidad
            guardar_inventario()
            actualizar_lista()
            limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Ingrese el nombre de la fruta.")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida. Ingrese un número entero.")

def eliminar_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    if fruta in inventario:
        del inventario[fruta]
        guardar_inventario()
        actualizar_lista()
        limpiar_campos()
    else:
        messagebox.showinfo("Eliminar", f"La fruta '{fruta}' no existe.")

def editar_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    try:
        cantidad = int(entrada_cantidad.get())
        if fruta in inventario:
            inventario[fruta] = cantidad
            guardar_inventario()
            actualizar_lista()
            limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", f"La fruta '{fruta}' no está registrada.")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida.")

def disminuir_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    try:
        cantidad = int(entrada_cantidad.get())
        if fruta in inventario:
            if cantidad <= inventario[fruta]:
                inventario[fruta] -= cantidad
                guardar_inventario()
                actualizar_lista()
                limpiar_campos()
                if inventario[fruta] == 0:
                    messagebox.showinfo("Aviso", f"'{fruta}' ahora tiene 0 unidades.")
            else:
                messagebox.showwarning("Advertencia", "Cantidad mayor a la disponible.")
        else:
            messagebox.showinfo("Aviso", "Fruta no encontrada.")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida.")

def buscar_fruta(*args):
    consulta = entrada_busqueda.get().strip().lower()
    lista_frutas.delete(0, tk.END)
    for fruta, cantidad in inventario.items():
        if consulta in fruta.lower():
            lista_frutas.insert(tk.END, f"{fruta}: {cantidad}")

def seleccionar_fruta(event):
    seleccion = lista_frutas.curselection()
    if seleccion:
        item = lista_frutas.get(seleccion[0])
        fruta, cantidad = item.split(":")
        entrada_fruta.delete(0, tk.END)
        entrada_fruta.insert(0, fruta.strip())
        entrada_cantidad.delete(0, tk.END)
        entrada_cantidad.insert(0, cantidad.strip())

def actualizar_lista():
    lista_frutas.delete(0, tk.END)
    for fruta, cantidad in sorted(inventario.items()):
        lista_frutas.insert(tk.END, f"{fruta}: {cantidad}")

def limpiar_campos():
    entrada_fruta.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)

# ---------- Modo oscuro / claro ----------
def toggle_modo_oscuro():
    if modo_oscuro.get():
        colores["bg"] = "#2b2b2b" # Fondo oscuro para modo oscuro
        colores["fg"] = "#ffffff" # Texto blanco en modo oscuro
        colores["entry_bg"] = "#3a3a3a" # Fondo de entrada en modo oscuro
        colores["list_bg"] = "#3a3a3a" # Fondo de lista de modo oscuro
        estilo.configure("TButton", background="#4caf50", foreground="white") # Color de botón para modo oscuro
    else:
        colores["bg"] = "#d0ebff"     # Fono azul pastel
        colores["fg"] = "#000000"     # Texto negro en modo claro
        colores["entry_bg"] = "#e7f5ff" # Fondo de entrada en modo claro
        colores["list_bg"] = "#e7f5ff" # Fondo de lista en modo claro

    ventana.configure(bg=colores["bg"])
    for widget in ventana.winfo_children():
        if isinstance(widget, (ttk.Frame, ttk.Label)):
            widget.configure(style="TLabel")
        elif isinstance(widget, tk.Listbox):
            widget.configure(bg=colores["list_bg"], fg=colores["fg"])

    estilo.configure("TLabel", background=colores["bg"], foreground=colores["fg"], font=("Segoe UI", 10, "bold"))
    estilo.configure("TEntry", fieldbackground=colores["entry_bg"], foreground=colores["fg"])

# ---------- Inicialización ----------
cargar_inventario()

ventana = tk.Tk()
ventana.title("INVENTARIO DE FRUTAS")
ventana.geometry("580x650")

colores = {
    "bg": "#d0ebff",  # Color de fondo de la ventana (Azul pastel suave)
    "fg": "#000000",  # Color del texto (Negro)
    "entry_bg": "#e7f5ff",  # Color de fondo de las entradas de texto (Azul claro suave)
    "list_bg": "#e7f5ff"  # Color de fondo de las listas (Azul claro suave)
}

ventana.configure(bg=colores["bg"]) # Establece el color de fondo de la ventana

# ---------- Estilos ----------
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TLabel", background=colores["bg"], foreground=colores["fg"], font=("Segoe UI", 10, "bold"))
estilo.configure("TEntry", padding=5)
estilo.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))

# ---------- Sección Entrada ----------
frame_entrada = ttk.Frame(ventana)
frame_entrada.pack(pady=20)

ttk.Label(frame_entrada, text="Fruta:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entrada_fruta = ttk.Entry(frame_entrada, width=30)
entrada_fruta.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Cantidad:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entrada_cantidad = ttk.Entry(frame_entrada, width=30)
entrada_cantidad.grid(row=1, column=1, padx=5, pady=5)

# ---------- Botones ----------
frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10)

# Botones con colores personalizados
colores_botones = [
    ("Agregar", agregar_fruta, "#81c784"), # Verde claro para Agregar
    ("Editar", editar_fruta, "#64b5f6"), # Azul medio para Editar
    ("Eliminar", eliminar_fruta, "#e57373"), # Rojo claro para Eliminar
    ("Disminuir", disminuir_fruta, "#ffb74d"), # Naranja para Disminuir
]

for i, (texto, cmd, color) in enumerate(colores_botones):
    boton = tk.Button(frame_botones, text=texto, command=cmd,
                      bg=color, fg="white", font=("Segoe UI", 10, "bold"), width=12)
    boton.grid(row=0, column=i, padx=6)

# ---------- Buscar ----------
frame_busqueda = ttk.Frame(ventana)
frame_busqueda.pack(pady=15)

ttk.Label(frame_busqueda, text=" Buscar fruta:").pack()
entrada_busqueda = ttk.Entry(frame_busqueda, width=35)
entrada_busqueda.pack(pady=5)
entrada_busqueda.bind("<KeyRelease>", buscar_fruta)

# ---------- Inventario ----------
ttk.Label(ventana, text=" Inventario actual:", font=("Segoe UI", 10, "bold")).pack(pady=5)
lista_frutas = tk.Listbox(ventana, width=50, height=15, font=("Courier New", 10),
                          bg=colores["list_bg"], fg=colores["fg"])
lista_frutas.pack(pady=5)
lista_frutas.bind("<<ListboxSelect>>", seleccionar_fruta)

# ---------- Modo Oscuro ----------
modo_oscuro = tk.BooleanVar()
chk_oscuro = ttk.Checkbutton(ventana, text=" Modo oscuro", variable=modo_oscuro, command=toggle_modo_oscuro)
chk_oscuro.pack(pady=10)

# ---------- Iniciar vista ----------
actualizar_lista()
ventana.mainloop()