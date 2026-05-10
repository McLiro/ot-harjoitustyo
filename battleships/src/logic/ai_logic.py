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

    def process_sinking(self, coords: list):
        pass

class Medium(Ai):
    def __init__(self):
        super().__init__()
        self.checkerboard = self.create_checkerboard()
        self.target_stack = []
        self.current_direction = None

    def create_checkerboard(self):
        evens = [(x, y) for x in range(10) for y in range(10) if (x + y) % 2 == 0]
        odds  = [(x, y) for x in range(10) for y in range(10) if (x + y) % 2 != 0]
        return random.choice([evens, odds])

    def make_move(self):
        if self.target_stack:
            return self.target_mode_move()
        else:
            return self.hunt_mode_move()

    def hunt_mode_move(self):
        if not self.checkerboard:
            target = random.choice(self.unshot_coords)
        else:
            target = random.choice(self.checkerboard)
        self.unshot_coords.remove(target)
        if target in self.checkerboard:
            self.checkerboard.remove(target)
        return target

    def target_mode_move(self):
            for i in range(len(self.target_stack) - 1, -1, -1):
                current = self.target_stack[i]
                possible = self.unshot_neighbors(current)

                if not possible:
                    continue

                if self.current_direction is not None:
                    dx, dy = self.current_direction
                    line = [n for n in possible if
                            (n[0] - current[0], n[1] - current[1]) in ((dx, dy), (-dx, -dy))]
                    
                    if line:
                        possible = line
                    else:
                        continue

                chosen = random.choice(possible)

                self.unshot_coords.remove(chosen)
                if chosen in self.checkerboard:
                    self.checkerboard.remove(chosen)

                self.target_stack.append(self.target_stack.pop(i))
                
                return chosen

            if self.current_direction is not None:
                self.current_direction = None
                return self.target_mode_move()

            self.target_stack.clear()
            return self.hunt_mode_move()

    def unshot_neighbors(self, coord):
        x, y = coord
        candidates = [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]
        return [c for c in candidates
                if 0 <= c[0] < 10 and 0 <= c[1] < 10 and c in self.unshot_coords]

    def process_result(self, coords, result):
        if result == "MISS":
            pass
        elif result == "HIT":
            stack_size = len(self.target_stack)

            if stack_size == 0:
                self.target_stack.append(coords)
            elif stack_size == 1:
                prev = self.target_stack[-1]
                dx = coords[0] - prev[0]
                dy = coords[1] - prev[1]
                if dx != 0 or dy != 0:
                    self.current_direction = (dx // max(1, abs(dx)),
                                              dy // max(1, abs(dy)))
                self.target_stack.append(coords)
            else:
                self.target_stack.append(coords)
        elif result == "SINK":
            pass

    def process_sinking(self, coords: list):
            for cell in coords:
                while cell in self.target_stack:
                    self.target_stack.remove(cell)
            
            stack_size = len(self.target_stack)
            
            if stack_size == 0:
                self.current_direction = None
                
            elif stack_size == 1:
                self.current_direction = None
                
            else:
                prev = self.target_stack[-2]
                curr = self.target_stack[-1]
                
                dx = curr[0] - prev[0]
                dy = curr[1] - prev[1]
                
                if dx != 0 or dy != 0:
                    self.current_direction = (
                        dx // max(1, abs(dx)),
                        dy // max(1, abs(dy))
                    )
                else:
                    self.current_direction = None