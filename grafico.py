import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Mascota:
    def __init__(self, nombre, tipo, imagen_path):
        self.nombre = nombre
        self.tipo = tipo
        self.imagen_path = imagen_path
        self.felicidad = 50
        self.salud = 50
        self.hambre = 50
        self.cuidado_recibido = True  # Nuevo atributo para controlar el cuidado recibido
    
    def alimentar(self, cantidad):
        self.hambre -= cantidad
        if self.hambre <= 0:
            self.hambre = 0
        self.salud += cantidad * 0.1
        if self.salud > 100:
            self.salud = 100
        self.cuidado_recibido = True  # La mascota recibe cuidado al ser alimentada
    
    def jugar(self):
        self.felicidad += 20
        if self.felicidad > 100:
            self.felicidad = 100
        self.hambre += 10
        if self.hambre > 100:
            self.hambre = 100
        self.cuidado_recibido = True  # La mascota recibe cuidado al jugar
    
    def cuidar(self):
        self.salud += 15
        if self.salud > 100:
            self.salud = 100
        self.cuidado_recibido = True  # La mascota recibe cuidado al ser cuidada
    
    def descuido(self):
        if not self.cuidado_recibido:
            self.salud -= 5  # Reducción de salud por falta de cuidado
            self.hambre += 10  # Aumento de hambre por falta de cuidado
        self.cuidado_recibido = False  # Reiniciamos el estado de cuidado para el próximo ciclo

class Perro(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre, tipo="Perro", imagen_path="dog.png")
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando")

class Gato(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre, tipo="Gato", imagen_path="cat.png")
    
    def maullar(self):
        print(f"{self.nombre} está maullando")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def adoptar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def interactuar_mascota(self, nombre_mascota, accion):
        for mascota in self.mascotas:
            if mascota.nombre == nombre_mascota:
                if accion == "alimentar":
                    mascota.alimentar(20)
                    return f"Interacción completa con {mascota.nombre}."
                elif accion == "jugar":
                    mascota.jugar()
                    return f"Interacción completa con {mascota.nombre}."
                elif accion == "cuidar":
                    mascota.cuidar()
                    return f"Interacción completa con {mascota.nombre}."
                else:
                    return f"No se encontró la acción {accion}."
        return f"No se encontró una mascota con el nombre {nombre_mascota}."

    def __str__(self):
        return f"Usuario: {self.nombre}, Mascotas: {[mascota.nombre for mascota in self.mascotas]}"

class SimuladorDeMascotasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Mascotas")

        self.usuarios = []

        self.usuario_actual = None
        self.mascota_actual = None

        self.lbl_usuario = tk.Label(root, text="Nombre de Usuario:")
        self.lbl_usuario.grid(row=0, column=0)
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.grid(row=0, column=1)
        self.btn_registrar_usuario = tk.Button(root, text="Registrar Usuario", command=self.registrar_usuario)
        self.btn_registrar_usuario.grid(row=0, column=2)

        self.lbl_nombre_mascota = tk.Label(root, text="Nombre de Mascota:")
        self.lbl_nombre_mascota.grid(row=1, column=0)
        self.entry_nombre_mascota = tk.Entry(root)
        self.entry_nombre_mascota.grid(row=1, column=1)

        self.btn_adoptar_perro = tk.Button(root, text="Adoptar Perro", command=self.adoptar_perro)
        self.btn_adoptar_perro.grid(row=2, column=0)
        self.btn_adoptar_gato = tk.Button(root, text="Adoptar Gato", command=self.adoptar_gato)
        self.btn_adoptar_gato.grid(row=2, column=1)

        self.lista_mascotas = tk.Listbox(root)
        self.lista_mascotas.grid(row=3, column=0, columnspan=2)
        self.lista_mascotas.bind("<<ListboxSelect>>", self.seleccionar_mascota)

        self.btn_alimentar = tk.Button(root, text="Alimentar", command=self.interactuar_mascota_alimentar)
        self.btn_alimentar.grid(row=4, column=0)
        self.btn_jugar = tk.Button(root, text="Jugar", command=self.interactuar_mascota_jugar)
        self.btn_jugar.grid(row=4, column=1)
        self.btn_cuidar = tk.Button(root, text="Cuidar", command=self.interactuar_mascota_cuidar)
        self.btn_cuidar.grid(row=4, column=2)

        self.lbl_imagen = tk.Label(root)
        self.lbl_imagen.grid(row=5, column=0, columnspan=2)

        self.lbl_estado = tk.Label(root, text="Estado de la Mascota:")
        self.lbl_estado.grid(row=6, column=0, columnspan=2)

        self.lbl_salud = tk.Label(root, text="Salud: N/A")
        self.lbl_salud.grid(row=7, column=0, columnspan=2)
        self.lbl_felicidad = tk.Label(root, text="Felicidad: N/A")
        self.lbl_felicidad.grid(row=8, column=0, columnspan=2)
        self.lbl_hambre = tk.Label(root, text="Hambre: N/A")
        self.lbl_hambre.grid(row=9, column=0, columnspan=2)

        # Iniciar el ciclo de simulación de descuido
        self.simular_descuido()

    def registrar_usuario(self):
        nombre_usuario = self.entry_usuario.get()
        if nombre_usuario:
            usuario = Usuario(nombre_usuario)
            self.usuarios.append(usuario)
            self.usuario_actual = usuario
            messagebox.showinfo("Usuario Registrado", f"Usuario {nombre_usuario} registrado con éxito.")
        else:
            messagebox.showwarning("Error", "Debe ingresar un nombre de usuario.")

    def adoptar_perro(self):
        nombre_mascota = self.entry_nombre_mascota.get()
        if nombre_mascota:
            mascota = Perro(nombre_mascota)
            self.usuario_actual.adoptar_mascota(mascota)
            self.lista_mascotas.insert(tk.END, nombre_mascota)
            messagebox.showinfo("Adopción", f"Has adoptado un perro llamado {nombre_mascota}.")
        else:
            messagebox.showwarning("Error", "Debe ingresar un nombre para la mascota.")

    def adoptar_gato(self):
        nombre_mascota = self.entry_nombre_mascota.get()
        if nombre_mascota:
            mascota = Gato(nombre_mascota)
            self.usuario_actual.adoptar_mascota(mascota)
            self.lista_mascotas.insert(tk.END, nombre_mascota)
            messagebox.showinfo("Adopción", f"Has adoptado un gato llamado {nombre_mascota}.")
        else:
            messagebox.showwarning("Error", "Debe ingresar un nombre para la mascota.")

    def seleccionar_mascota(self, event):
        seleccion = self.lista_mascotas.curselection()
        if seleccion:
            nombre_mascota = self.lista_mascotas.get(seleccion)
            for mascota in self.usuario_actual.mascotas:
                if mascota.nombre == nombre_mascota:
                    self.mascota_actual = mascota
                    break
            self.actualizar_imagen_mascota()
            self.actualizar_estado_mascota()

    def actualizar_imagen_mascota(self):
        if self.mascota_actual:
            image = Image.open(self.mascota_actual.imagen_path)
            image = image.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.lbl_imagen.config(image=photo)
            self.lbl_imagen.image = photo

    def actualizar_estado_mascota(self):
        if self.mascota_actual:
            self.lbl_salud.config(text=f"Salud: {self.mascota_actual.salud}")
            self.lbl_felicidad.config(text=f"Felicidad: {self.mascota_actual.felicidad}")
            self.lbl_hambre.config(text=f"Hambre: {self.mascota_actual.hambre}")

    def interactuar_mascota_alimentar(self):
        if self.mascota_actual:
            mensaje = self.usuario_actual.interactuar_mascota(self.mascota_actual.nombre, "alimentar")
            messagebox.showinfo("Interacción", mensaje)
            self.actualizar_estado_mascota()

    def interactuar_mascota_jugar(self):
        if self.mascota_actual:
            mensaje = self.usuario_actual.interactuar_mascota(self.mascota_actual.nombre, "jugar")
            messagebox.showinfo("Interacción", mensaje)
            self.actualizar_estado_mascota()

    def interactuar_mascota_cuidar(self):
        if self.mascota_actual:
            mensaje = self.usuario_actual.interactuar_mascota(self.mascota_actual.nombre, "cuidar")
            messagebox.showinfo("Interacción", mensaje)
            self.actualizar_estado_mascota()

    def simular_descuido(self):
        def actualizar_estado():
            if self.mascota_actual:
                self.mascota_actual.descuido()
                self.actualizar_estado_mascota()
            self.root.after(5000, actualizar_estado)  # Actualizar cada 5 segundos

        actualizar_estado()
    
    def actualizar_estado_mascota(self):
        if self.mascota_actual:
            self.lbl_salud.config(text=f"Salud: {self.mascota_actual.salud}")
            self.lbl_felicidad.config(text=f"Felicidad: {self.mascota_actual.felicidad}")
            self.lbl_hambre.config(text=f"Hambre: {self.mascota_actual.hambre}")

            # Verificar estado de hambre
            if self.mascota_actual.hambre >= 100:
                messagebox.showwarning("Alerta", "Tu mascota tiene hambre. Aliméntala!")

            # Verificar estado de salud
            if self.mascota_actual.salud <= 0:
                messagebox.showwarning("Alerta", "Cuida a tu mascota. Su salud está muy baja.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorDeMascotasApp(root)
    root.mainloop()