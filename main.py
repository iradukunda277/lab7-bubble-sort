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


def visualize_bubble_sort(numbers: list[int], delay: float = 0.5) -> list[int]:
    """Visualize Bubble Sort step by step in the terminal."""
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            clear_screen()
            print("Bubble Sort Visualization\n")
            print(f"Pass {i + 1} | Comparing positions {j} and {j + 1}\n")
            display_bars(sorted_numbers, (j, j + 1))
            time.sleep(delay)

            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )
                swapped = True

                clear_screen()
                print("Bubble Sort Visualization\n")
                print(f"Swap done between positions {j} and {j + 1}\n")
                display_bars(sorted_numbers, (j, j + 1))
                time.sleep(delay)

        if not swapped:
            break

    clear_screen()
    print("Sorting complete.\n")
    display_bars(sorted_numbers)
    return sorted_numbers


def main() -> None:
    numbers = [8, 3, 1, 7, 4, 6, 2, 5]

    print("Original list:", numbers)
    input("\nPress Enter to start the terminal visualization...")

    sorted_numbers = visualize_bubble_sort(numbers, delay=0.4)

    print("\nSorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
