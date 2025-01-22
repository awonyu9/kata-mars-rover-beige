from rover import Rover


def test_move_forward_north():
    rover = Rover(4, 2, "north")
    rover.move_forward()

    assert (rover.x == 4) and (rover.y == 3)

def test_move_forward_west():
    rover = Rover(4, 2, "west")
    rover.move_forward()

    assert (rover.x == 3) and (rover.y == 2)

def test_move_forward_south():
    rover = Rover(4, 2, "south")
    rover.move_forward()

    assert (rover.x == 4) and (rover.y == 1)

def test_move_forward_east():
    rover = Rover(4, 2, "east")
    rover.move_forward()

    assert (rover.x == 5) and (rover.y == 2)
