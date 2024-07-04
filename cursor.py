import cv2
import numpy as np

def find_blue_cursor_position(frame):
    # Criar uma máscara para acor azul com os critérios especificados
    lower_blue = np.array([0, 0,129])
    upper_blue = np.array([63, 63,255])
    mask = cv2.inRange(frame, lower_blue, upper_blue)

    # Encontrar a primeira posição da cor azul de cima para baixo
    indices = np.where(mask == 255)
    if len(indices[0]) > 0 and len(indices[1]) > 0:
        y = indices[0][0]
        x = indices[1][0]
        return (x, y)
    else:
        return None

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
        position = find_blue_cursor_position(frame)

        # Desenhar o cursor virtual (bola vermelha) se a posição foi encontrada
        if position is not None:
            cv2.circle(frame, position, 10, (0, 0, 255), -1)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality - Blue Cursor Detection', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
