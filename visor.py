import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps  
import os

class VisorImagenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        
   
        self.imagen_label = tk.Label(root)
        self.imagen_label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.boton_cargar = tk.Button(self.frame, text="Cargar Imagen", command=self.cargar_imagen)
        self.boton_cargar.pack(side=tk.LEFT)

        self.boton_grayscale = tk.Button(self.frame, text="Escala de Grises", command=self.aplicar_grayscale)
        self.boton_grayscale.pack(side=tk.LEFT)

        self.boton_invert = tk.Button(self.frame, text="Invertir Colores", command=self.invertir_colores)
        self.boton_invert.pack(side=tk.LEFT)

        self.imagen_actual = None

    def cargar_imagen(self):
        ruta_imagen = filedialog.askopenfilename()
        if ruta_imagen:
            self.imagen_actual = Image.open(ruta_imagen)
            self.mostrar_imagen(self.imagen_actual)

    def mostrar_imagen(self, imagen):
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.imagen_label.configure(image=imagen_tk)
        self.imagen_label.image = imagen_tk

    def aplicar_grayscale(self):
        if self.imagen_actual:
            imagen_gris = ImageOps.grayscale(self.imagen_actual)
            self.mostrar_imagen(imagen_gris)
        else:
            messagebox.showerror("Error", "No se ha cargado ninguna imagen")

    def invertir_colores(self):
        if self.imagen_actual:
            imagen_invertida = ImageOps.invert(self.imagen_actual.convert("RGB"))
            self.mostrar_imagen(imagen_invertida)
        else:
            messagebox.showerror("Error", "No se ha cargado ninguna imagen")

if __name__ == "__main__":
    root = tk.Tk()
    app = VisorImagenes(root)
    root.mainloop()