import cv2
import numpy as np
#pip install opencv-python
def invert_colors(frame):
    return cv2.bitwise_not(frame)

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)

        # Inverter as cores
        frame = invert_colors(frame)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality - Inverted Colors', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

