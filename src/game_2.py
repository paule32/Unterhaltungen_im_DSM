# ----------------------------------------------------------------------------
# Datei:  game.py
# Author: Jens Kallup - paule32
#
# Rechte: (c) 2024 by kallup non-profit software
#         all rights reserved
#
# only for education, and for non-profit usage !!!
# commercial use ist not allowed.
# ----------------------------------------------------------------------------
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 480

WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symmetrische Hexagone mit 45 Grad Drehung")

def draw_hexagon_with_border(surface, fill_color, border_color, center, size):
    angle = 360 / 6
    points = []
    for i in range(6):
        x = center[0] + size * math.cos(math.radians(angle * i + 30))  # 30 Grad für die Drehung
        y = center[1] + size * math.sin(math.radians(angle * i + 30))
        points.append((x, y))
    pygame.draw.polygon(surface, fill_color, points)
    pygame.draw.lines(surface, border_color, True, points, 2)

hexagon_size = 32
rows = 8
cols = 8

x_offset = 1.5 * hexagon_size
y_offset = hexagon_size * math.sqrt(3) / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    for row in range(rows):
        for col in range(cols):
            x = col * 2 * hexagon_size + (row % 2) * hexagon_size + x_offset
            y = row * hexagon_size * math.sqrt(3) + y_offset
            draw_hexagon_with_border(screen, GREEN, BLACK, (x, y + 18), hexagon_size)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
