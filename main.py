import random
from typing import Generator


def bubble_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy of the list using Bubble Sort."""
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )
                swapped = True

        if not swapped:
            break

    return sorted_numbers


def bubble_sort_steps(
    numbers: list[int],
) -> Generator[tuple[list[int], tuple[int, int] | None, int], None, None]:
    """
    Yield Bubble Sort states for visualization.

    Returns:
        current list,
        active pair being compared,
        sorted_start index (everything from this index to the end is sorted)
    """
    arr = numbers.copy()
    n = len(arr)

    if n == 0:
        yield arr.copy(), None, 0
        return

    for i in range(n):
        swapped = False
        sorted_start = n - i  # suffix already sorted from previous passes

        for j in range(0, n - i - 1):
            yield arr.copy(), (j, j + 1), sorted_start

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr.copy(), (j, j + 1), sorted_start

        if not swapped:
            yield arr.copy(), None, 0
            return

    yield arr.copy(), None, 0


def build_numbers(size: int = 40) -> list[int]:
    """Create a shuffled list 1..size."""
    numbers = list(range(1, size + 1))
    random.shuffle(numbers)
    return numbers


def run_visualization(size: int = 40, delay_ms: int = 80) -> None:
    """Run the Pygame Bubble Sort visualization."""
    try:
        import pygame
    except ImportError:
        print("Pygame is not installed.")
        print("Run: pip install pygame")
        return

    pygame.init()

    width, height = 1100, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bubble Sort Visualization")

    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont("consolas", 28, bold=True)
    info_font = pygame.font.SysFont("consolas", 18)

    background_color = (10, 12, 24)
    bar_color = (102, 204, 255)  # light blue
    active_color = (255, 215, 0)  # yellow
    sorted_color = (120, 255, 160)  # green
    text_color = (245, 245, 245)

    numbers = build_numbers(size)
    steps = bubble_sort_steps(numbers)

    current_numbers = numbers.copy()
    active_pair = None
    sorted_start = len(numbers)

    paused = False
    finished = False
    running = True
    last_update = pygame.time.get_ticks()
    speed_multiplier = 1  # 1x, 2x, 3x, or 4x speed

    def draw_scene() -> None:
        screen.fill(background_color)

        title = title_font.render("Bubble Sort Visualization", True, text_color)
        screen.blit(title, (30, 20))

        if finished:
            status_text = "Finished"
        elif paused:
            status_text = "Paused"
        else:
            status_text = "Sorting..."

        info = info_font.render(
            f"Status: {status_text}   |   SPACE = pause/resume   |   R = restart   |   1/2/3/4 = speed   |   Q / ESC = quit",
            True,
            text_color,
        )
        screen.blit(info, (30, 60))

        speed_text = info_font.render(f"Speed: x{speed_multiplier}", True, text_color)
        screen.blit(speed_text, (30, 90))

        if not current_numbers:
            pygame.display.flip()
            return

        margin_x = 40
        top_y = 130
        bottom_margin = 40
        draw_height = height - top_y - bottom_margin
        draw_width = width - (2 * margin_x)

        n = len(current_numbers)
        max_value = max(current_numbers)

        step_width = draw_width / n
        bar_width = max(4, int(step_width) - 2)

        for i, value in enumerate(current_numbers):
            bar_height = int((value / max_value) * draw_height)
            x = int(margin_x + i * step_width)
            y = height - bottom_margin - bar_height

            color = bar_color

            if i >= sorted_start:
                color = sorted_color

            if active_pair is not None and i in active_pair and not finished:
                color = active_color

            pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))

        pygame.display.flip()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

                elif event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.key == pygame.K_r:
                    numbers = build_numbers(size)
                    steps = bubble_sort_steps(numbers)
                    current_numbers = numbers.copy()
                    active_pair = None
                    sorted_start = len(numbers)
                    paused = False
                    finished = False
                    last_update = pygame.time.get_ticks()

                elif event.key == pygame.K_1:
                    speed_multiplier = 1

                elif event.key == pygame.K_2:
                    speed_multiplier = 2

                elif event.key == pygame.K_3:
                    speed_multiplier = 3

                elif event.key == pygame.K_4:
                    speed_multiplier = 4

        now = pygame.time.get_ticks()

        if not paused and not finished and now - last_update >= delay_ms // speed_multiplier:
            try:
                current_numbers, active_pair, sorted_start = next(steps)
            except StopIteration:
                finished = True
                active_pair = None
                sorted_start = 0

            last_update = now

        draw_scene()

    pygame.quit()


def main() -> None:
    run_visualization(size=40, delay_ms=80)


if __name__ == "__main__":
    main()
