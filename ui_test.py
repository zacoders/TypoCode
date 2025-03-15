# import pygame
# import pygame_gui

# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# manager = pygame_gui.UIManager((400, 300))
# button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((150, 130), (100, 50)),
#     text='Нажми',
#     manager=manager
# )

# clock = pygame.time.Clock()
# running = True
# while running:
#     time_delta = clock.tick(60) / 1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         manager.process_events(event)

#         # Проверяем, нажата ли кнопка
#         if event.type == pygame_gui.UI_BUTTON_PRESSED:
#             if event.ui_element == button:  # Если нажали именно нашу кнопку
#                 print("Кнопка нажата!")

#     manager.update(time_delta)
#     screen.fill((0, 0, 0))
#     manager.draw_ui(screen)
#     pygame.display.update()
