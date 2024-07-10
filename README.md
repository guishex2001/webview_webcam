# Proyecto de Streaming de Webcam en WebView

Este proyecto combina un servidor de streaming de webcam utilizando Flask y OpenCV, y una ventana de vista web (WebView) que abarca todas las pantallas conectadas utilizando `pywebview`. La ventana WebView muestra el stream de la webcam en tiempo real.

## Estructura del Proyecto

carpeta_raiz/
│
├── main.py
├── templates/
│ └── index.html

markdown
Copiar código

## Requisitos

- Python 3.6 o superior
- Las siguientes bibliotecas de Python:
  - `pywebview`
  - `screeninfo`
  - `opencv-python`
  - `flask`

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
Crea un entorno virtual (opcional pero recomendado):

sh
Copiar código
python -m venv venv
Activa el entorno virtual:

En Windows:
sh
Copiar código
venv\Scripts\activate
En macOS/Linux:
sh
Copiar código
source venv/bin/activate
Instala las dependencias:

sh
Copiar código
pip install pywebview screeninfo opencv-python flask
Uso
Asegúrate de tener todos los archivos en su lugar:

main.py
index.html dentro de la carpeta templates
Ejecuta el archivo main.py:

sh
Copiar código
python main.py
Esto iniciará el servidor Flask y abrirá una ventana WebView que mostrará el stream de la webcam en tiempo real y abarcará todas las pantallas conectadas.