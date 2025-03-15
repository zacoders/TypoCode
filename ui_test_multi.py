import pygame
import pygame_gui

pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Multiple Windows with Buttons')

# Set up GUI manager
manager = pygame_gui.UIManager(window_size)

# Create first window with buttons
window_1 = pygame_gui.elements.UIWindow(
    rect=pygame.Rect(50, 50, 300, 200),
    manager=manager,
    window_display_title='Window 1'
)
button_1_1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(10, 40, 100, 30),
    text='Button 1.1',
    manager=manager,
    container=window_1
)
button_1_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(10, 80, 100, 30),
    text='Button 1.2',
    manager=manager,
    container=window_1
)

# Create second window with buttons
window_2 = pygame_gui.elements.UIWindow(
    rect=pygame.Rect(400, 50, 300, 200),
    manager=manager,
    window_display_title='Window 2'
)
button_2_1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(10, 40, 100, 30),
    text='Button 2.1',
    manager=manager,
    container=window_2
)
button_2_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(10, 80, 100, 30),
    text='Button 2.2',
    manager=manager,
    container=window_2
)

# Main loop
clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60) / 1000.0  # Time in seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # Handle events for pygame_gui elements
        manager.process_events(event)

    # Update GUI
    manager.update(time_delta)

    # Draw everything
    screen.fill((255, 255, 255))  # Clear screen
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
