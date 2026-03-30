import os
import time


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def display_bars(
    numbers: list[int], active_indices: tuple[int, int] | None = None
) -> None:
    """Display the list as ASCII bars in the terminal."""
    if active_indices is None:
        active_indices = (-1, -1)

    for index, value in enumerate(numbers):
        marker = " <==" if index in active_indices else ""
        print(f"{value:2} | {'#' * value}{marker}")


def bubble_sort(numbers: list[int]) -> list[int]:
    """Return a sorted copy of the list using Bubble Sort.

    TODO:
    - Add support for `key` parameter for direct element keying.
    - Add `reverse` flag for descending order.
    - Add unit tests for empty, single-element, sorted, reverse lists.
    """
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    # early exit for trivial cases
    if n <= 1:
        return sorted_numbers

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )
                swapped = True

        # if nothing swapped in this pass, the list is already sorted
        if not swapped:
            break

    return sorted_numbers


def visualize_bubble_sort(numbers: list[int], delay: float = 0.5) -> list[int]:
    """Visualize Bubble Sort step by step in the terminal.

    TODO:
    - Add optional `step_mode` (press Enter per compare) as an interactive mode.
    - Add `max_width` scaling to avoid huge bars for large values.
    - Add colored output for active vs sorted region.
    """
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    for i in range(n):
        swapped = False

        # small improvement: show pass summary once per pass
        clear_screen()
        print("Bubble Sort Visualization")
        print(f"Pass {i + 1}/{n} | Remaining unsorted tail length: {n - i - 1}\n")
        display_bars(sorted_numbers, active_indices=None)
        time.sleep(delay)

        for j in range(0, n - i - 1):
            clear_screen()
            print("Bubble Sort Visualization")
            print(f"Pass {i + 1}/{n} | Comparing positions {j} and {j + 1}\n")
            display_bars(sorted_numbers, (j, j + 1))
            time.sleep(delay)

            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )
                swapped = True

                clear_screen()
                print("Bubble Sort Visualization")
                print(f"Pass {i + 1}/{n} | Swap between positions {j} and {j + 1}\n")
                display_bars(sorted_numbers, (j, j + 1))
                time.sleep(delay)

        if not swapped:
            # TODO: highlight the early-exit optimization in visualization
            break

    clear_screen()
    print("Sorting complete.\n")
    display_bars(sorted_numbers)
    return sorted_numbers


def main() -> None:
    # TODO: accept a CLI argument or random generated list for more flexible testing
    numbers = [8, 3, 1, 7, 4, 6, 2, 5]

    print("Original list:", numbers)
    input("\nPress Enter to start the terminal visualization...")

    sorted_numbers = visualize_bubble_sort(numbers, delay=0.4)

    print("\nSorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
