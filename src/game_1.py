import pygame
import sys
import math

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 600, 500

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)

# Erstellung des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symmetrische Hexagone mit Rahmen")

# Funktion zum Zeichnen eines Hexagons mit Rahmen
def draw_hexagon_with_border(surface, fill_color, border_color, center, size):
    angle = 360 / 6
    points = []
    for i in range(6):
        x = center[0] + size * math.cos(math.radians(angle * i))
        y = center[1] + size * math.sin(math.radians(angle * i))
        points.append((x, y))
    pygame.draw.polygon(surface, fill_color, points)
    pygame.draw.lines(surface, border_color, True, points, 2)

# Größe und Anzahl der Hexagone im Gitter
hexagon_size = 32
rows = 8
cols = 8

# Berechnung des horizontalen und vertikalen Versatzes für die Zentrierung
x_offset = 1.5 * hexagon_size
y_offset = hexagon_size * math.sqrt(3) / 2

# Hauptspielschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrund zeichnen
    screen.fill(WHITE)

    # Hexagone mit Rahmen zeichnen
    for row in range(rows):
        for col in range(cols):
            x = col * 2 * hexagon_size + (row % 2) * hexagon_size + x_offset
            y = row * hexagon_size * math.sqrt(3) + y_offset
            draw_hexagon_with_border(screen, GREEN, BLACK, (x, y+20), hexagon_size)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
