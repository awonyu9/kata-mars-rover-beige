from rover import Rover
import pytest


test_data_movement_forward = [
    ("north", 4, 2, 4, 3),
    ("west", 4, 2, 3, 2),
    ("south", 4, 2, 4, 1),
    ("east", 4, 2, 5, 2)
]

test_data_movement_backward = [
    ("north", 4, 2, 4, 1),
    ("west", 4, 2, 5, 2),
    ("south", 4, 2, 4, 3),
    ("east", 4, 2, 3, 2)
]

test_data_turn_left = [
    ("north", "west"),
    ("west", "south"),
    ("south", "east"),
    ("east", "north")
]

test_data_turn_right = [
    ("north", "east"),
    ("east", "south"),
    ("south", "west"),
    ("west", "north")
]

@pytest.mark.parametrize("direction, x, y, expected_x, expected_y", test_data_movement_forward)
def test_move_forward(direction, x, y, expected_x, expected_y):
    rover = Rover(x, y, direction)
    rover.move_forward()

    assert (rover.x == expected_x) and (rover.y == expected_y)

@pytest.mark.parametrize("direction, x, y, expected_x, expected_y", test_data_movement_backward)
def test_move_backward(direction, x, y, expected_x, expected_y):
    rover = Rover(x, y, direction)
    rover.move_backward()

    assert (rover.x == expected_x) and (rover.y == expected_y)

@pytest.mark.parametrize("initial_direction, expected_direction", test_data_turn_left)
def test_turn_left(initial_direction, expected_direction):
    rover = Rover(4, 2, initial_direction)
    rover.turn_left()

    assert rover.direction == expected_direction

@pytest.mark.parametrize("initial_direction, expected_direction", test_data_turn_right)
def test_turn_right(initial_direction, expected_direction):
    rover = Rover(4, 2, initial_direction)
    rover.turn_right()

    assert rover.direction == expected_direction
