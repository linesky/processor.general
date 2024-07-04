import cv2
import pygame
import numpy as np
import random
import time
#pip install opencv-python pygame numpy
# Configurações dos fogos de artifício
class Firework:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.particles = []
        self.explosion_time = time.time() + random.uniform(0.5, 1.5)
        self.create_firework()

    def create_firework(self):
        self.x = random.randint(0, self.width)
        self.y = random.randint(self.height // 2, self.height)
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
        self.particles.append([self.x, self.y, self.color])

    def update(self):
        if time.time() >= self.explosion_time:
            self.explode()
        self.draw_particles()

    def explode(self):
        new_particles = []
        for particle in self.particles:
            x, y, color = particle
            for _ in range(100):
                angle = random.uniform(0, 2 * np.pi)
                speed = random.uniform(1, 5)
                dx = np.cos(angle) * speed
                dy = np.sin(angle) * speed
                new_particles.append([x, y, dx, dy, color])
        self.particles = new_particles
        self.explosion_time = time.time() + random.uniform(1, 2)

    def draw_particles(self):
        new_particles = []
        for particle in self.particles:
            if len(particle) == 3:
                x, y, color = particle
                pygame.draw.circle(self.screen, color, (x, y), 3)
                new_particles.append(particle)
            else:
                x, y, dx, dy, color = particle
                x += dx
                y += dy
                dx *= 0.95
                dy *= 0.95
                if dx**2 + dy**2 > 1:
                    new_particles.append([x, y, dx, dy, color])
                    pygame.draw.circle(self.screen, color, (int(x), int(y)), 2)
        self.particles = new_particles

def draw_fireworks(screen, width, height, fireworks):
    for firework in fireworks:
        firework.update()

def main():
    # Inicializar Pygame
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Augmented Reality - Fireworks')

    # Inicializar OpenCV
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    fireworks = [Firework(screen, width, height) for _ in range(5)]

    while True:
        # Capturar frame da câmera
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)

        # Converter o frame para um formato que Pygame possa usar
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)

        # Desenhar o frame da câmera
        screen.blit(frame, (0, 0))

        # Atualizar e desenhar fogos de artifício
        draw_fireworks(screen, width, height, fireworks)

        # Atualizar a tela do Pygame
        pygame.display.flip()

        # Manter o FPS constante
        pygame.time.delay(2)
        #fireworks = [Firework(screen, width, height) for _ in range(5)]
        # Verificar eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return

if __name__ == "__main__":
    main()

