import tkinter as tk

ventana=tk.Tk()
ventana.title("Mi primera ventana")
etiqueta=tk.Label(ventana,text="no hablo con malos amigos,chao")
etiqueta.pack(pady=20)
ventana.mainloop()