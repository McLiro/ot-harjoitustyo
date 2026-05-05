from sprites.ui import Ship

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

    def hit(self, coords):
        self.hp -= 1

        if self.hp == 0:
            self.is_sunk = True
            return ("SUNK", self)
        
        return ("HIT", coords)
    
    def create_sprite(self, x, y):
        if self.rotation == "H":
            sprite = Ship(x, y, self.length, 1, 50)
        else:
            sprite = Ship(x, y, 1, self.length, 50)

        return sprite