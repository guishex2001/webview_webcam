import os
import webview
from screeninfo import get_monitors
import threading
import cv2
from flask import Flask, render_template, Response

class WebViewWindow:
    def __init__(self):
        self.current_url = "http://localhost:5000/"

        # Obtener información sobre las pantallas
        monitors = get_monitors()

        # Obtener el ancho y alto total de todas las pantallas
        total_width = sum(monitor.width for monitor in monitors)
        total_height = max(monitor.height for monitor in monitors)

        # Obtener la posición de la pantalla principal
        primary_monitor = next((monitor for monitor in monitors if monitor.is_primary), None)
        if primary_monitor:
            x, y = primary_monitor.x, primary_monitor.y
        else:
            # Si no se detecta una pantalla principal, usar la primera pantalla como referencia
            x, y = monitors[0].x, monitors[0].y

        # Configurar la ventana para abarcar todas las pantallas desde la posición de la pantalla principal
        self.window = webview.create_window(
            "WebView Window",
            url=self.current_url,
            width=total_width,
            height=total_height,
            frameless=True,
            easy_drag=False,
            x=x,
            y=y
        )

def gen_frames():
    camera = cv2.VideoCapture(0)  # Captura de la cámara web (índice 1, cambiar a 0 si es necesario)

    # Ajustar la resolución de la cámara para mejorar la calidad
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Ancho deseado, ajustar según la capacidad de la cámara
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Alto deseado, ajustar según la capacidad de la cámara

    while True:
        success, frame = camera.read()  # Leer el frame de la cámara
        if not success:
            break
        else:
            # Ajustar la calidad del JPEG para mejorar la imagen
            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def run_flask_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    window = WebViewWindow()
    webview.start()
