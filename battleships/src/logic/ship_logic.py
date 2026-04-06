class ShipLogic:
    def __init__(self, x, y, length, rotation):
        self.x = x
        self.y = y
        self.length = length
        self.rotation = rotation
        self.hp = length
        self.is_sunk = False
