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
