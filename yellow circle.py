import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    v = 10  # пикселей в секунду
    fps = 300
    screen.fill('blue')
    pygame.display.flip()
    drawing = False
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                r = 0
                x, y = event.pos
        if drawing:
            r += v / fps
            clock.tick(fps)
            pygame.draw.circle(screen, 'yellow', (x, y), r)
            pygame.display.flip()
        screen.fill('blue')
    pygame.quit()