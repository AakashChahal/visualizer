from pydoc import describe
from turtle import clear
import pygame
import random
import math
pygame.init()


class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    GREY = 125, 125, 125
    GRADIENTS = [
        (100, 100, 100),
        (150, 150, 150),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont('comicsans', 20)
    LRG_FONT = pygame.font.SysFont('SFPro', 40)
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
        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.WHITE)
    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start sorting", 1, draw_info.BLACK)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 5))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD / 2, draw_info.TOP_PAD, draw_info.width -
                      draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)

        pygame.draw.rect(draw_info.window, draw_info.WHITE, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * \
            draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n: int, min_val: int, max_val: int) -> list:
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    n, min_val, max_val = 50, 1, 100
    run = True
    clock = pygame.time.Clock()
    draw_info = DrawInfo(
        800, 600, lst=generate_starting_list(n, min_val, max_val))
    sorting = False
    ascending = True
    pygame.display.update()

    while run:
        clock.tick(120)
        if sorting:
            try:
                next(algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                algo_generator = bubble_sort(draw_info, ascending)

    pygame.quit()


def bubble_sort(draw_info, ascending=True) -> list:
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst) - 1 - i):
            n1 = lst[j]
            n2 = lst[j + 1]

            if n1 > n2 and ascending:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN,
                          j+1: draw_info.RED}, True)
                yield True

    return lst


def insertion_sort(draw_info, ascending=True) -> list:
    lst = draw_info.lst

    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1] and ascending:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            draw_list(draw_info, {j: draw_info.GREEN,
                      j-1: draw_info.RED}, True)
            yield True
            j -= 1

    return lst


# def selection_sort(draw_info, ascending=True) -> list:
#     lst = draw_info.lst

#     for i in range(len(lst)):
#         min_index = i
#         for j in range(i, len(lst)):
#             if lst[j] < lst[min_index] and ascending:
#                 min_index = j
#         lst[i], lst[min_index] = lst[min_index], lst[i]
#         draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED})
#         yield True

#     return lst


if __name__ == "__main__":
    main()
