import pygame


pygame.init()
SIZE = (460, 835)
screen = pygame.display.set_mode(SIZE)

display = 0
iphone = pygame.image.load('iPhone2.jpg').convert_alpha()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 211, 79)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

check = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        x, y = pygame.mouse.get_pos()

        if display == 0:
            screen.blit(iphone, pygame.Rect(0, 0, 100, 100))
            pygame.draw.rect(screen, WHITE, (0, 0, 23, 835))
            pygame.draw.rect(screen, WHITE, (428, 0, 30, 835))
            pygame.draw.polygon(screen, WHITE, ((22, 0), (22, 45), (60, 0)))

            pygame.draw.rect(screen, GOLD, (40, 98, 365, 650))

            if 65 <= x <= 380 and 600 <= y <= 650:
                pygame.draw.rect(screen, (200, 200, 200), (65, 600, 315, 50))
            else:
                pygame.draw.rect(screen, WHITE, (65, 600, 315, 50))

            if event.type == pygame.MOUSEBUTTONDOWN and 65 <= x <= 380 and 600 <= y <= 650:
                display = 1

        elif display == 1:
            screen.blit(iphone, pygame.Rect(0, 0, 100, 100))
            pygame.draw.rect(screen, WHITE, (0, 0, 23, 835))
            pygame.draw.rect(screen, WHITE, (428, 0, 30, 835))
            pygame.draw.polygon(screen, WHITE, ((22, 0), (22, 45), (60, 0)))

            pygame.draw.rect(screen, (255, 211, 79), (40, 98, 365, 650))
            pygame.draw.rect(screen, WHITE, (60, 118, 325, 450))

            pygame.draw.line(screen, (45, 101, 255), (60, 343), (385, 343))
            pygame.draw.line(screen, GOLD, (223, 343), (223, 568))
            pygame.draw.line(screen, GOLD, (60, 456), (385, 456))

            if 60 <= x <= 222 and 344 <= y <= 456:
                pygame.draw.rect(screen, (200, 200, 200), (60, 344, 163, 112))
            elif 223 <= x <= 385 and 344 <= y <= 456:
                pygame.draw.rect(screen, (200, 200, 200), (223, 344, 163, 112))
            elif 223 <= x <= 385 and 456 <= y <= 568:
                pygame.draw.rect(screen, (200, 200, 200), (223, 456, 163, 112))
            elif 60 <= x <= 222 and 456 <= y <= 568:
                pygame.draw.rect(screen, (200, 200, 200), (60, 456, 163, 112))

            if event.type == pygame.MOUSEBUTTONDOWN and 60 <= x <= 222 and 344 <= y <= 456:
                for x in range(3000):
                    pygame.draw.rect(screen, RED, (60, 344, 163, 112))
                    pygame.draw.rect(screen, GREEN, (223, 344, 163, 112))
                    pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN and 223 <= x <= 385 and 344 <= y <= 456:
                for x in range(3000):
                    pygame.draw.rect(screen, GREEN, (223, 344, 163, 112))
                    pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN and 223 <= x <= 385 and 456 <= y <= 568:
                for x in range(3000):
                    pygame.draw.rect(screen, RED, (223, 456, 163, 112))
                    pygame.draw.rect(screen, GREEN, (223, 344, 163, 112))
                    pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN and 60 <= x <= 222 and 456 <= y <= 568:
                for x in range(3000):
                    pygame.draw.rect(screen, RED, (60, 456, 163, 112))
                    pygame.draw.rect(screen, GREEN, (223, 344, 163, 112))
                    pygame.display.flip()

            if (x - 380)**2 + (y - 725)**2 <= 400:
                pygame.draw.circle(screen, (200, 200, 200), (380, 725), 20)
            else:
                pygame.draw.circle(screen, WHITE, (380, 725), 20)

            if event.type == pygame.MOUSEBUTTONDOWN and (x - 380)**2 + (y - 725)**2 <= 400:
                display = 0

    pygame.display.flip()

pygame.quit()
