import pygame
import pygame_gui

pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size, pygame.NOFRAME)  # Remove window bar
pygame.display.set_caption('Full-Screen Window Example')

# Set up GUI manager
manager = pygame_gui.UIManager(window_size)

# Create a "window" surface (for simulating full-screen UI windows)
window_1_surface = pygame.Surface(window_size)
window_2_surface = pygame.Surface(window_size)

# Create buttons on each window
button_open_window_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(300, 250, 200, 50),
    text='Open Window 2',
    manager=manager
)

button_close_window_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(300, 250, 200, 50),
    text='Close Window 2',
    manager=manager
)

# Initially, window 2 surface is hidden
window_2_surface.fill((0, 0, 155))  # Fill window 2 with blue (as a background color)
window_1_surface.fill((0, 150, 0))  # Fill window 1 with green (as a background color)

# Initially, window 2 is hidden
window_2_visible = False

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
                window_2_visible = True  # Show the second "window"
            elif event.ui_element == button_close_window_2:
                window_2_visible = False  # Hide the second "window"

    # Clear screen
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the appropriate "window"
    if window_2_visible:
        screen.blit(window_2_surface, (0, 0))  # Show window 2
    else:
        screen.blit(window_1_surface, (0, 0))  # Show window 1

    # Update the GUI manager
    manager.update(time_delta)

    # Draw UI elements (buttons)
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
