import cv2
import numpy as np

def find_blue_cursor_position(frame):
    # Criar uma máscara para acor azul com os critérios especificados
    
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

        # Procurar a posição do cursor azul
        

        # Desenhar o cursor virtual (bola vermelha) se a posição foi encontrada

        # Mostrar a imagem
        lower_blue = (0,0,129)
        upper_blue = (63,63,255)
        frame = cv2.inRange(frame, lower_blue, upper_blue)
        cv2.imshow('Augmented Reality - Blue Cursor Detection', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
