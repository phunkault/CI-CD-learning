import pytest

from src.heap.heap import MinHeap


# Arrange
@pytest.fixture()
def heap():
    return MinHeap()


# Initial state
def test_heap_initial_state(heap):
    # Assert
    assert heap
    assert not heap.container
    assert heap.size == 0
    assert heap.is_empty
    assert not heap.peek()


# Str
def test_heap_to_str(heap):
    # Assert
    assert str(heap) == '[]'


# Find
def test_min_heap_find_empty_heap(heap):
    # Act
    result = heap.find(1)

    # Assert
    assert result == []


def test_min_heap_find_value_not_present(heap):
    # Arrange
    heap.push(5).push(3).push(8).push(2).push(7).push(3)

    # Act
    result = heap.find(6)

    # Assert
    assert result == []


def test_min_heap_find_value_present(heap):
    # Arrange
    heap.push(5).push(3).push(8).push(2).push(7).push(3)

    # Act
    result = heap.find(3)

    # Assert
    assert result == [1, 2]


def test_min_heap_find_single_element_heap(heap):
    # Arrange
    heap.push(42)

    # Act
    result = heap.find(42)

    assert result == [0]


# Push
def test_push_one_element(heap):
    # Act
    heap.push(4)

    # Assert
    assert heap.size == 1
    assert not heap.is_empty
    assert heap.peek() == 4


def test_push_multiple_elements(heap):
    # Arrange
    heap.push(2)

    # Act
    heap.push(7).push(1).push(5)

    # Assert
    assert heap.size == 4
    assert heap.peek() == 1


# Replace
def test_replace_in_empty_heap(heap):
    # Act
    assert not heap.replace()


def test_replace_in_heap_with_one_element(heap):
    # Arrange
    heap.push(1)
    # Act
    replaced_value = heap.replace()

    # Assert
    assert replaced_value == 1
    assert heap.size == 0
    assert not heap.peek()


def test_replace_in_heap_with_several_elements(heap):
    # Arrange
    heap.push(1).push(2).push(3).push(4).push(5).push(6).push(7)

    # Act
    replaced_value = heap.replace()

    # Assert
    assert replaced_value == 1
    assert heap.size == 6
    assert heap.peek() == 2


# Remove
def test_min_heap_remove_empty_heap(heap):
    # Act
    heap.remove(5)

    # Assert
    assert heap.container == []


def test_min_heap_remove_nonexistent_value(heap):
    # Arrange
    heap.push(5).push(3).push(8).push(2).push(7)

    # Act
    heap.remove(4)

    # Assert
    assert heap.container == [2, 3, 8, 5, 7]


def test_min_heap_remove_single_element_heap(heap):
    # Assert
    heap.push(5)

    # Act
    heap.remove(5)

    # Assert
    assert heap.container == []


def test_min_heap_remove_last_element(heap):
    # Arrange
    heap.push(5).push(3).push(8).push(2).push(7)

    # Act
    heap.remove(7)

    # Assert
    assert heap.container == [2, 3, 8, 5]


def test_min_heap_remove_middle_element(heap):
    # Arrange
    heap.push(5).push(3).push(8).push(2).push(7)

    # Act
    heap.remove(3)

    assert heap.container == [2, 5, 8, 7]


def test_min_heap_remove_multiple_occurrences(heap):
    # Arrange
    heap.push(5).push(3).push(8).push(2).push(7).push(3)

    # Act
    heap.remove(3)

    # Assert
    assert heap.container == [2, 5, 8, 7]
