import pygame
import sys
import math

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 640, 480

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Erstellung des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symmetrische Hexagone mit 3D-Effekt")

# Funktion zum Zeichnen eines Hexagons mit räumlichem 3D-Effekt
def draw_hexagon_3d_perspective(surface, center, size, rotation_angle, perspective_factor):
    angle = 360 / 6
    points = []
    for i in range(6):
        x = center[0] + size * math.cos(math.radians(angle * i + rotation_angle))
        y = center[1] + size * math.sin(math.radians(angle * i + rotation_angle))
        points.append((x, y))
    
    # Perspektivische Darstellung
    for i in range(3):
        points[i] = (points[i][0], points[i][1] - perspective_factor * size)
        points[i + 3] = (points[i + 3][0], points[i + 3][1] - perspective_factor * size)
    
    pygame.draw.polygon(surface, RED, [points[0], points[1], points[2], points[5]])
    pygame.draw.polygon(surface, YELLOW, [points[2], points[3], points[4], points[5]])
    pygame.draw.polygon(surface, BLUE, [points[1], points[2], points[3]])
    
    pygame.draw.lines(surface, BLACK, True, points, 2)
    
# Funktion zum Zeichnen eines kleinen blauen Dreiecks mit rechtem Winkel
def draw_blue_triangle_1(surface, position_1, size):
    x, y = position_1
    points_1 = [
        (x, y-25),
        (x + size, y),
        (x - 10, y - size)
    ]
    pygame.draw.polygon(surface, BLUE, points_1)

# Größe und Anzahl der Hexagone im Gitter
hexagon_size = 32
rows = 8
cols = 8

# Berechnung des horizontalen und vertikalen Versatzes für die Zentrierung
x_offset = 1.5 * hexagon_size
y_offset = hexagon_size * math.sqrt(3) / 2

# Rotationswinkel
rotation_angle = 90  # Ursprünglicher Rotationswinkel

# Perspektivenfaktor - beeinflusst die Intensität der Perspektive
perspective_factor = 0.2

# Hauptspielschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrund zeichnen
    screen.fill(WHITE)

    # Hexagone mit räumlichem 3D-Effekt zeichnen
    for row in range(rows):
        for col in range(cols):
            x = col * 2 * hexagon_size + (row % 2) * hexagon_size + x_offset
            y = row * hexagon_size * math.sqrt(3) + y_offset
            x += 20
            y += 20
            draw_hexagon_3d_perspective(screen, (x, y), hexagon_size, rotation_angle, perspective_factor)
            draw_blue_triangle_1(screen, (x-5, y-10), 0)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
