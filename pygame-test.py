from lib import main as wekoptics
import pygame


pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
running = True

circle = wekoptics.CircleLens(x=150, y=250, radius=100, curvate=100, rotation=0)
circle2 = wekoptics.CircleLens(x=350, y=250, radius=50, curvate=100, rotation=0)
rect = wekoptics.Rect(x=400, y=50, w=80, h=40, rotation=0)

font = pygame.font.SysFont(None, 24)

def display_gui(circle):
    global screen
    pygame.draw.line(screen, (255, 255, 255), (0, 250), (500, 250))
    pygame.draw.line(screen, (255, 255, 255), (250, 0), (250, 500))
    txt = font.render(str(circle.rotation) + "° angle", True, (255, 255,255))
    screen.blit(txt, (40, 40))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    circle.rotation = wekoptics.angles_summ(circle.rotation, 1)
    circle2.rotation = wekoptics.angles_summ(circle.rotation, 1)
    rect.rotation = wekoptics.angles_summ(rect.rotation, 1)

    circle.render()
    circle2.render()
    rect.render()

    pygame.draw.polygon(screen, (170, 170, 255), circle.pygame_points())
    pygame.draw.polygon(screen, (170, 170, 255), circle2.pygame_points())
    pygame.draw.polygon(screen, (170, 170, 255), rect.pygame_points())

    display_gui(circle)

    pygame.display.flip()
    clock.tick(100)
pygame.quit()