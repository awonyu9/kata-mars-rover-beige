class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move_forward(self):
        match self.direction:
            case "north":
                self.y += 1
            case "west":
                self.x -= 1
      