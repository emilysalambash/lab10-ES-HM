import pygame
import random


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        mole_width, mole_height = mole_image.get_size()

        window_width = 32 * 20
        window_height = 32 * 16
        screen = pygame.display.set_mode((640, 512))
        color = (0, 0, 0)

        def draw_grid():
            for x in range(0, window_width, 32):
                pygame.draw.line(screen, color, (x, 0), (x, window_height))
            for y in range(0, window_height, 32):
                pygame.draw.line(screen, color, (0, y), (window_width, y))
        clock = pygame.time.Clock()
        running = True

        mole_x, mole_y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x * 32 <= mouse_x < (mole_x + 1) * 32 and mole_y * 32 <= mouse_y < (mole_y + 1) * 32:
                        mole_x, mole_y = random.randrange(0, 20), random.randrange(0, 16)
            screen.fill("light green")
            draw_grid()
            # You can draw the mole with this snippet:
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * 32, mole_y * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
