import cv2
import pyautogui
import numpy as np
import time
import sys

codec = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
out = None
recording = False
start_time = None

# Dimensiones del cuadrado
square_x = 100
square_y = 100
square_size = 50


def start_recording():
    global out, recording, start_time

    # Abrir el archivo de video para grabación
    out = cv2.VideoWriter("Grabacion.mp4", codec, 60, (1366, 768))

    # Iniciar el tiempo de grabación
    start_time = time.time()
    recording = True


def stop_recording():
    global out, recording, start_time

    # Detener la grabación y cerrar el archivo de video
    out.release()
    recording = False

    # Reiniciar el tiempo de grabación
    start_time = None

    # Mostrar un mensaje de finalización
    print("Grabación finalizada. Se ha creado el archivo Grabacion.mp4.")

    # Salir del programa
    sys.exit()


def draw_square(frame):
    # Dibujar el cuadrado en el marco
    cv2.rectangle(frame, (square_x, square_y), (square_x + square_size, square_y + square_size), (0, 255, 0), 2)


# Crear la ventana de visualización
cv2.namedWindow("Grabando", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Grabando", 480, 270)

# Iniciar la grabación automáticamente
start_recording()

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Dibujar el cuadrado en el marco
    draw_square(frame)

    if recording:
        # Mostrar el tiempo de grabación en el marco
        elapsed_time = time.time() - start_time
        cv2.putText(frame, f"Tiempo: {int(elapsed_time)}s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Guardar el marco en el archivo de video
        out.write(frame)

        # Detener la grabación después de 10 segundos
        if elapsed_time >= 10:
            stop_recording()

    cv2.imshow('Grabando', frame)

    key = cv2.waitKey(25)

    # Mover el cuadrado usando las teclas de flecha
    if key == ord('w'):
        square_y -= 10
    elif key == ord('s'):
        square_y += 10
    elif key == ord('a'):
        square_x -= 10
    elif key == ord('d'):
        square_x += 10

    if cv2.getWindowProperty('Grabando', cv2.WND_PROP_VISIBLE) < 1:  # Salir si se cierra la ventana
        if recording:
            stop_recording()
        break

cv2.destroyAllWindows()
