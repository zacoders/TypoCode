import pygame
import pygame_gui

pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Window Toggle Example')

# Set up GUI manager
manager = pygame_gui.UIManager(window_size)

# Create first window (it will be visible initially)
window_1 = pygame_gui.elements.UIWindow(
    rect=pygame.Rect(0, 0, window_size[0], window_size[1]),
    manager=manager,
    window_display_title='Window 1',
    resizable=False,
    draggable=False,
    
)

button_open_window_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(300, 250, 200, 50),
    text='Open Window 2',
    manager=manager,
    container=window_1
)

# Create second window (it is hidden initially)
window_2 = pygame_gui.elements.UIWindow(
    rect=pygame.Rect(0, 0, window_size[0], window_size[1]),
    manager=manager,
    window_display_title='Window 2',
    resizable=False
)
button_close_window_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(300, 250, 200, 50),
    text='Close Window 2',
    manager=manager,
    container=window_2
)

# Initially, window 2 is hidden
window_2.hide()

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

        # Check if the button to open the second window is clicked
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button_open_window_2:
                window_1.hide()  # Hide the first window
                window_2.show()  # Show the second window
            elif event.ui_element == button_close_window_2:
                window_2.hide()  # Hide the second window
                window_1.show()  # Show the first window

    # Update GUI
    manager.update(time_delta)

    # Draw everything
    screen.fill((255, 255, 255))  # Clear screen
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
