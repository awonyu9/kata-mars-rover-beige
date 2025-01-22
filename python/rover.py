map_max_y = 10
map_min_y = -10
map_max_x = 10
map_min_x = -10

class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move_forward(self):
        match self.direction:
            case "north":
                if self.y == map_max_y:
                    self.y *= -1
                else:
                    self.y += 1
            case "west":
                if self.x == map_min_x:
                    self.x *= -1
                else:
                    self.x -= 1
            case "south":
                if self.y == map_min_y:
                    self.y *= -1
                else:
                    self.y -= 1
            case "east":
                if self.x == map_max_x:
                    self.x *= -1
                else:
                    self.x += 1

    def move_backward(self):
        match self.direction:
            case "north":
                self.y -= 1
            case "west":
                self.x += 1
            case "south":
                self.y += 1
            case "east":
                self.x -= 1
        
    def turn_left(self):
        directions = ["north", "west", "south", "east"]
        direction_index = directions.index(self.direction)
        new_direction_index = (direction_index + 1) % 4
        self.direction = directions[new_direction_index]

    def turn_right(self):
        directions = ["north", "west", "south", "east"]
        direction_index = directions.index(self.direction)
        new_direction_index = (direction_index - 1) % 4
        self.direction = directions[new_direction_index]
      