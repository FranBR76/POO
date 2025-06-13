import tkinter as tk

root = tk.Tk()

img = tk.PhotoImage(file="enersync/imgs/plano.png")  # Caminho da imagem
label = tk.Label(root, image=img)
label.pack()

root.mainloop()
