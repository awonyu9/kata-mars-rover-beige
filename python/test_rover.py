from rover import Rover


def test_move_forward():
    rover = Rover(4, 2, "north")
    rover.move_forward()

    assert (rover.x == 4) and (rover.y == 3)
