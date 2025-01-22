Feature: Moving forward

Scenario: Facing North

  Given The rover has position (x=4, y=2) and facing North
  When Rover moves forward
  Then The rover has position (x=4, y=3) and facing North

Scenario: Facing West

  Given The rover has position (x=4, y=2) and facing West
  When Rover moves forward
  Then The rover has position (x=3, y=2) and facing West

Scenario: Facing South

  Given The rover has position (x=4, y=2) and facing South
  When Rover moves forward
  Then The rover has position (x=4, y=1) and facing South

Scenario: Facing East

  Given The rover has position (x=4, y=2) and facing East
  When Rover moves forward
  Then The rover has position (x=5, y=2) and facing East

// ---

Feature: Moving backward

| Direction | Initial X | Initial Y | Expected X | Expected Y |
---------------------------------------------------------------
| North     | 4         | 3         | 4          | 1          |
| West      | 4         | 2         | 5          | 2          |
| South     | 4         | 2         | 4          | 3          |
| East      | 4         | 2         | 3          | 2          |

// ---

Feature: Turning left

| Initial Direction | Expected Direction |
------------------------------------------
| North             | West               |
| West              | South              |
| South             | East               |
| East              | North              |

// ---

Feature: Turning right

| Initial Direction | Expected Direction |
------------------------------------------
| North             | East               |
| East              | South              |
| South             | West               |
| West              | North              |

// ---

Implicit stuff:

- 2D
- discrete movement (one cell moves)
- No diagonal moves
