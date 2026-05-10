from logic.ai_logic import Easy, Medium

def test_easy_ai():
    ai = Easy()

    ai.make_move()
    ai.process_result((2, 2), "MISS")
    ai.process_sinking([(2,2), (2,3)])

def test_medium_ai_miss():
    ai = Medium()

    ai.make_move()
    ai.process_result((2, 2), "MISS")

def test_medium_ai_hit():
    ai = Medium()

    ai.make_move()
    ai.process_result((2, 2), "HIT")

def test_medium_ai_target_mode():
    ai = Medium()

    ai.make_move()
    ai.process_result((2, 2), "HIT")
    ai.make_move()

def test_medium_ai_sinking():
    ai = Medium()

    ai.make_move()
    ai.process_result((2, 3), "HIT")
    ai.process_result((2, 2), "SUNK")
    ai.process_sinking([(2,2), (2,3)])

def test_medium_ai_perpendicular_ship():
    ai = Medium()

    ai.process_result((2, 2), "HIT")
    ai.process_result((2, 3), "HIT")
    ai.process_result((2, 4), "HIT")
    ai.process_result((2, 5), "MISS")
    ai.process_result((2, 1), "SUNK")
    ai.process_sinking([(2,1),(2,2),(2,3)])

def test_medium_ai_perpendicular_ship_two_hits():
    ai = Medium()

    ai.process_result((2, 2), "HIT")
    ai.process_result((2, 3), "HIT")
    ai.process_result((2, 4), "HIT")
    ai.process_result((2, 5), "HIT")
    ai.process_result((2, 1), "SUNK")
    ai.process_sinking([(2,1),(2,2),(2,3)])

def test_medium_stack_sizes():
    ai = Medium()

    ai.process_result((2, 2), "HIT")
    ai.process_result((2, 3), "HIT")
    ai.process_result((2, 4), "HIT")

def test_medium_no_checkerboard():
    ai = Medium()

    ai.checkerboard = []

    ai.make_move()

def test_medium_target_mode_no_stack():
    ai = Medium()

    ai.current_direction = (1, 1)

    ai.target_mode_move()

def test_medium_target_mode_with_stack():
    ai = Medium()

    ai.target_stack = [(1,1)]
    ai.current_direction = (1, 1)
    ai.target_mode_move()

def test_medium_incorrect_result():
    ai = Medium()

    ai.process_result((2,2), "ASDF")
