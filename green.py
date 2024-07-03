import cv2
import numpy as np
#pip install opencv-python
def apply_blue_effect(frame):
    # Separar os canais de cor
    blue_channel, green_channel, red_channel = cv2.split(frame)
    
    # Definir o canal red para o valor máximo
    green_channel[:] = 255
    
    # Combinar os canais novamente
    frame = cv2.merge([blue_channel, green_channel, red_channel])
    return frame

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

        # Aplicar o efeito azul
        frame = apply_blue_effect(frame)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality - Blue Effect', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

