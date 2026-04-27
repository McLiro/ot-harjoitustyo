class ShipLogic:
    """Handles the logical attributes of a ship.

    Attributes:
        x: X-axis coordinate.
        y: Y-axis coordinate.
        length: Length of the ship.
        rotation: Rotation of the ship, either horizontal or vertical.
        hp: Hitpoints, equal to the length of the ship.
        is_sunk: Boolean for sunken ships.
    """
    def __init__(self, x, y, length, rotation):
        self.x = x
        self.y = y
        self.length = length
        self.rotation = rotation
        self.hp = length
        self.is_sunk = False
