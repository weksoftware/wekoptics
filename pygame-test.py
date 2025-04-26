from lib import main as wekoptics
import pygame


pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
running = True

circle = wekoptics.CircleLens(x=250, y=250, radius=100, rotation=90)
rect = wekoptics.Rect(x=400, y=50, w=80, h=40, rotation=45)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    circle.rotation = wekoptics.angles_summ(circle.rotation, 1)
    rect.rotation = wekoptics.angles_summ(rect.rotation, 1)

    circle.render()
    rect.render()

    pygame.draw.polygon(screen, (170, 170, 255), circle.pygame_points())
    pygame.draw.polygon(screen, (170, 170, 255), rect.pygame_points())


    pygame.display.flip()
    clock.tick(100)
pygame.quit()