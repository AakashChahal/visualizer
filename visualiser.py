import pygame
import random
pygame.init()


class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    GREY = 125, 125, 125
    GRADIENTS = [
        (0, 100, 200),
        (250, 100, 50),
        (192, 192, 0)
    ]
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width: int, height: int, lst: list) -> None:
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst: list) -> None:
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round(
            (self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.WHITE)
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * \
            draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))


def generate_starting_list(n: int, min_val: int, max_val: int) -> list:
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    draw_info = DrawInfo(800, 600, lst=generate_starting_list(50, 1, 100))
    run = True
    clock = pygame.time.Clock()
    pygame.display.update()
    while run:
        clock.tick(60)
        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
