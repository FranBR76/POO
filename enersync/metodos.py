import tkinter as tk


class Voltar:
    def voltar(self):
        self.root.destroy()
        from app import App
        root = tk.Tk()
        app = App(root, self.id_usuario)
        root.mainloop()