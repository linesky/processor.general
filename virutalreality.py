import cv2
import numpy as np

def draw_grid(frame, grid_size):
    height, width, _ = frame.shape
    step_x = width // grid_size
    step_y = height // grid_size

    # Desenhar linhas verticais
    for x in range(0, width, step_x):
        cv2.line(frame, (x, 0), (x, height), (255, 255, 255), 1)

    # Desenhar linhas horizontais
    for y in range(0, height, step_y):
        cv2.line(frame, (0, y), (width, y), (255, 255, 255), 1)

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    grid_size = 16

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)

        # Desenhar a grade
        draw_grid(frame, grid_size)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality Grid', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

