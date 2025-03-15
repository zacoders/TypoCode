import pygame
import pygame_gui

# Инициализация Pygame и Pygame GUI
pygame.init()
window_surface = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600))

# Список для выбора
items = ['Опция 1', 'Опция 2', 'Опция 3', 'Опция 4']
selection_list = pygame_gui.elements.UISelectionList(
    relative_rect=pygame.Rect(100, 100, 200, 100),
    item_list=items,
    manager=manager
)

# Главный игровой цикл
running = True
while running:
    time_delta = pygame.time.get_ticks() / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обрабатываем события выбора элемента
        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            selected_item = selection_list.get_single_selection()
            if selected_item:
                print(f"Вы выбрали: {selected_item}")

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.fill((255, 255, 255))  # Белый фон
    manager.draw_ui(window_surface)

    pygame.display.update()

pygame.quit()
