import random

class Ai():
    def __init__(self):
        self.unshot_coords = [(x, y) for x in range(10) for y in range(10)]

class Easy(Ai):
    def __init__(self):
        super().__init__()

    def make_move(self):
        target = random.choice(self.unshot_coords)

        self.unshot_coords.remove(target)

        return target
    
    def process_result(self, coords, result):
        pass # Easy difficulty shoots randomly and does not react to hits.

class Medium(Ai):
    def __init__(self, board):
        super().__init__(board)