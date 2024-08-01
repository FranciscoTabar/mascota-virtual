# mascota-virtual
Este proyecto es una aplicación de escritorio desarrollada con Python y Tkinter que simula el cuidado de mascotas virtuales. Los usuarios pueden adoptar mascotas, alimentarlas, jugar con ellas y cuidar de su salud. La aplicación también simula el efecto del descuido en el estado de las mascotas.

Características
Registro de Usuarios: Permite registrar múltiples usuarios.
Adopción de Mascotas: Los usuarios pueden adoptar perros y gatos.
Interacciones con las Mascotas: Alimentar, jugar y cuidar a las mascotas para mantener su salud, felicidad y reducir el hambre.
Simulación de Descuido: La salud y el hambre de las mascotas se ven afectadas si no se les brinda cuidado constante.
Interfaz Gráfica: Interfaz amigable desarrollada con Tkinter, incluyendo imágenes de las mascotas.

Estructura del Código
Clase Mascota: Define los atributos y métodos básicos para cualquier mascota.
Clases Perro y Gato: Heredan de Mascota y añaden comportamientos específicos.
Clase Usuario: Maneja la información del usuario y las mascotas adoptadas.
Clase SimuladorDeMascotasApp: Crea la interfaz gráfica y maneja la lógica de la aplicación.

Requisitos
Python 3.x
Tkinter
PIL (Pillow)

Instalación
Clona el repositorio.

git clone https://github.com/FraciscoTabar/simulador-de-mascotas.git

Instala las dependencias.
 
pip install pillow

Ejecución
Para ejecutar la aplicación, navega al directorio del proyecto y ejecuta el script principal:

 
python simulador_de_mascotas.py

Uso
Registra un usuario ingresando un nombre y haciendo clic en "Registrar Usuario".
Ingresa el nombre de una mascota y selecciona "Adoptar Perro" o "Adoptar Gato".
Selecciona la mascota adoptada de la lista para interactuar con ella.
Usa los botones "Alimentar", "Jugar" y "Cuidar" para mantener el bienestar de tu mascota.
Observa los cambios en la salud, felicidad y hambre de tu mascota en la interfaz.

Autor
Desarrollado por Frank.
