import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))  # Создаём окно для обработки событий

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Проверяем, была ли нажата клавиша
            print(f'{event.key=}, {event.scancode=}')  # Выводим номер клавиши


pygame.quit()
