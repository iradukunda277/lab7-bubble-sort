from main import bubble_sort


def test_empty_list() -> None:
    assert bubble_sort([]) == []


def test_single_element() -> None:
    assert bubble_sort([5]) == [5]


def test_already_sorted() -> None:
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_order() -> None:
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_unsorted_list() -> None:
    assert bubble_sort([8, 3, 1, 7, 4]) == [1, 3, 4, 7, 8]