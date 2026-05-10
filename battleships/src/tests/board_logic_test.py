import unittest
from logic.board_logic import BoardLogic
from logic.ship_logic import ShipLogic

def test_init():
    board = BoardLogic(10)

    assert board.board_size == 10
    assert len(board.ships) == 0

def test_valid_ship():
    board = BoardLogic(10)
    horizontal_ship = ShipLogic(0, 0, 2, "H")
    vertical_ship = ShipLogic(4, 4, 3, "V")

    board.place_ship(horizontal_ship)

    assert len(board.ships) == 1

    board.place_ship(vertical_ship)

    assert len(board.ships) == 2

def test_out_of_bounds_ship():
    board = BoardLogic(10)
    out_of_bounds_ship = ShipLogic(8, 8, 5, "H")

    board.place_ship(out_of_bounds_ship)

    assert len(board.ships) == 0

def test_overlapping_ship():
    board = BoardLogic(10)
    valid_ship = ShipLogic(2, 2, 3, "V")
    overlapping_ship = ShipLogic(1, 3, 4, "H")

    board.place_ship(valid_ship)

    assert len(board.ships) == 1

    board.place_ship(overlapping_ship)

    assert len(board.ships) == 1

def test_board_reset():
    board = BoardLogic(10)
    ship = ShipLogic(2, 2, 3, "V")

    board.place_ship(ship)

    assert len(board.ships) == 1

    board.reset_board()

    assert len(board.ships) == 0

def test_ai_board_generation():
    board = BoardLogic(10)

    board.generate_board([5, 4, 3, 3, 2])

    assert len(board.ships) == 5

def test_shot_validation():
    board = BoardLogic(10)
    ship = ShipLogic(2, 2, 3, "V")
    board.place_ship(ship)

    board.validate_shot((2, 2))
    board.validate_shot((9, 9))
    board.validate_shot((2, 2))
    board.validate_shot((15, 15))

    assert len(board.shots) == 2
    assert ship.hp == 2

def test_loss_detection():
    board = BoardLogic(10)
    ship = ShipLogic(2, 2, 2, "V")
    board.place_ship(ship)

    board.validate_shot((2, 2))

    assert board.has_lost() == False

    board.validate_shot((2, 3))

    assert board.has_lost() == True

def test_to_dict():
    board = BoardLogic(10)
    ship = ShipLogic(2, 2, 2, "V")
    board.place_ship(ship)

    board.to_dict()

def test_from_dict():
    board = BoardLogic(10)
    ship = ShipLogic(2, 2, 2, "V")
    board.place_ship(ship)

    ship = ShipLogic(6, 6, 2, "H")
    board.place_ship(ship)

    dict = board.to_dict()
    board.from_dict(dict)

def test_ship_sprite_creation():
    ship = ShipLogic(2, 2, 2, "V")

    ship.create_sprite(100, 100)

    ship = ShipLogic(2, 2, 2, "H")

    ship.create_sprite(500, 500)