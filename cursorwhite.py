import cv2
import numpy as np
global xxx
global yyy
xxx=640-1
yyy=480-1
sets=0
def find_blue_cursor_position(frame):
    global xxx
    global yyy
    
    
    for yy in range(480):
        
            
        for xx in range(640):
            
            blue_channel,green_channel,red_channel=frame[xx,yy]
            if blue_channel>128 and green_channel>128 and red_channel>128:
                
                return (xx, yy)
            
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
