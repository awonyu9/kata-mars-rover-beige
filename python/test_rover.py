from rover import Rover
import pytest


test_data = [
    ("north", 4, 2, 4, 3),
    ("west", 4, 2, 3, 2),
    ("south", 4, 2, 4, 1),
    ("east", 4, 2, 5, 2)
]

@pytest.mark.parametrize("direction, x, y, expected_x, expected_y", test_data)
def test_move_forward_north(direction, x, y, expected_x, expected_y):
    rover = Rover(x, y, direction)
    rover.move_forward()

    assert (rover.x == expected_x) and (rover.y == expected_y)
