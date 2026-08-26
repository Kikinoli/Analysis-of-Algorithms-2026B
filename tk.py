import tkinter as tk


def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Enrique"
    lbl.config(text=f"¡Hola, {nombre}!")

root = tk.Tk()
root.title("Saludador de Compas")
root.geometry("360x220")  # Corregido: geometry

lbl = tk.Label(root, text="Escribe tu nombre y presiona el botón:")
lbl.pack(pady=10)  # Corregido: uso correcto de .pack()

entrada = tk.Entry(root)
entrada.pack(pady=10)

btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)

root.mainloop()
 