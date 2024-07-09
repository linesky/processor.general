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
            
            blue_channel,green_channel,red_channel=frame[yy,xx]
            if blue_channel>80 and green_channel>80 and red_channel<64:
                
                frame[yy,xx]=[255,255,255]
            
            else:
                frame[yy,xx]=[0,0,0]
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
        frame = find_blue_cursor_position(frame)

        
        # Mostrar a imagem
        cv2.imshow('Augmented Reality - Blue Cursor Detection', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
