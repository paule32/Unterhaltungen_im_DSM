import pygame
import pygame.gfxdraw
import sys
import math

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 800

# Farben
WHITE = (255, 255, 255)

# Erstellung des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot-Menge mit Farbübergang")

# Funktion zum Prüfen, ob ein Punkt in der Mandelbrot-Menge liegt
def mandelbrot(c, max_iterations):
    z = complex(0, 0)
    for i in range(max_iterations):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iterations

# Funktion zum Zeichnen des Mandelbrot-Fraktals mit Farbübergang
def draw_mandelbrot(surface, max_iterations, start_color, end_color):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Normalisierte Koordinaten im Bereich [-2, 2] x [-2, 2]
            re = (x - WIDTH / 2) / (WIDTH / 4)
            im = (y - HEIGHT / 2) / (HEIGHT / 4)

            # Mandelbrot-Komplexzahl
            c = complex(re, im)

            # Iterationen berechnen
            iterations = mandelbrot(c, max_iterations)

            # Farbübergang basierend auf den Iterationen
            color = (
                int(start_color[0] + (end_color[0] - start_color[0]) * iterations / max_iterations),
                int(start_color[1] + (end_color[1] - start_color[1]) * iterations / max_iterations),
                int(start_color[2] + (end_color[2] - start_color[2]) * iterations / max_iterations)
            )

            # Pixel zeichnen
            pygame.gfxdraw.pixel(surface, x, y, color)

# Hauptspielschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrund zeichnen
    screen.fill(WHITE)

    # Farbübergänge definieren
    start_color = (0, 0, 0)
    end_color = (255, 255, 255)

    # Mandelbrot-Fraktal mit Farbübergang zeichnen
    draw_mandelbrot(screen, 100, start_color, end_color)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
