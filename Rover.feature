Feature: Moving forward

Scenario: Facing North

  Given The rover has position (x=4, y=2) and facing North
  When Rover moves forward
  Then The rover has position (x=4, y=3) and facing North

Scenario: Facing West
...

// ---

Implicit stuff:

- 2D
- discrete movement (one cell moves)
- No diagonal moves
