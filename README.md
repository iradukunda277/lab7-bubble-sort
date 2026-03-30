# lab7-bubble-sort

A Python project that implements the Bubble Sort algorithm with a real-time Pygame visualization. Watch as the sorting algorithm bubbles larger values to the right, with interactive speed controls and intuitive keyboard navigation.

## Features

- ✅ **Bubble Sort Implementation** - Clean, testable core algorithm
- ✅ **Pygame Visualization** - Real-time graphical visualization with color-coded bars
- ✅ **Speed Controls** - Adjust sorting speed with keys 1 (x1), 2 (x2), 3 (x3), 4 (x4)
- ✅ **Pause/Resume** - Pause the sorting to observe specific states
- ✅ **Interactive Controls** - Restart, quit, and navigate easily
- ✅ **Test Coverage** - Comprehensive pytest test suite

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. Clone or download this project
2. Install dependencies:

```bash
pip install pygame pytest
```

## How to Run

### Run the Visualization

Start the interactive Pygame visualization:

```bash
python main.py
```

### Run Tests

Execute the test suite to verify the `bubble_sort()` function:

```bash
pytest test_main.py -v
```

Or simply:

```bash
pytest
```

## Keyboard Controls

While the visualization is running, use these keyboard shortcuts:

| Key | Action |
|-----|--------|
| **1** | Set speed to x1 (slowest) |
| **2** | Set speed to x2 |
| **3** | Set speed to x3 |
| **4** | Set speed to x4 (fastest) |
| **SPACE** | Pause/resume sorting animation |
| **R** | Restart with a new random array |
| **Q** or **ESC** | Quit the visualization |

## Understanding the Visualization

- **Light Blue Bars** - Regular unsorted elements
- **Yellow Bars** - Elements currently being compared
- **Green Bars** - Elements in their final sorted position
- **Speed Display** - Current playback speed shown in top-left corner

## Project Structure

```
lab7-bubble-sort/
├── main.py              # Bubble Sort implementation + Pygame visualization
├── test_main.py         # Pytest test suite
├── README.md            # This file
├── REPORT.md            # Project documentation and learning reflections
└── .github/             # Configuration files
```

## Code Quality

- All functions include docstrings
- Type hints used throughout for clarity
- Tests verify edge cases: empty lists, single elements, sorted arrays, reverse-sorted arrays
- Clean separation between core algorithm and visualization

## Learn More

The `bubble_sort()` function is the core sorting algorithm. It can be used independently:

```python
from main import bubble_sort

numbers = [8, 3, 1, 7, 4, 6, 2, 5]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8]
```