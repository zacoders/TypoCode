import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("Какая-то клавиша нажата!")

    # keys = pygame.key.get_pressed()

    # if any(keys[i] for i in range(len(keys))):
    #     if keys[pygame.KEYDOWN]:
    #         print("Какая-то клавиша нажата!")

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
