import pygame
import sys
import math

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600

# Farben
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Erstellung des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Koch-Schneeflocken-Fraktal")

# Funktion zum Zeichnen des Koch-Schneeflocken-Fraktals
def draw_koch_snowflake(surface, order, start_point, end_point):
    if order == 0:
        pygame.draw.line(surface, BLUE, start_point, end_point, 2)
    else:
        # Berechne die Punkte des gleichseitigen Dreiecks
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]

        p1 = (start_point[0] + delta_x / 3, start_point[1] + delta_y / 3)
        p2 = (start_point[0] + delta_x / 2 + math.sqrt(3) * delta_y / 6, start_point[1] + delta_y / 2 - math.sqrt(3) * delta_x / 6)
        p3 = (start_point[0] + 2 * delta_x / 3, start_point[1] + 2 * delta_y / 3)

        # Berechne die neuen Punkte für die Teilsegmente
        draw_koch_snowflake(surface, order - 1, start_point, p1)
        draw_koch_snowflake(surface, order - 1, p1, p2)
        draw_koch_snowflake(surface, order - 1, p2, p3)
        draw_koch_snowflake(surface, order - 1, p3, end_point)

# Hauptspielschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrund zeichnen
    screen.fill(WHITE)

    # Start- und Endpunkte für das Fraktal
    start_point = (100, 500)
    end_point = (700, 500)

    # Rekursiv das Koch-Schneeflocken-Fraktal zeichnen
    draw_koch_snowflake(screen, 4, start_point, end_point)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
