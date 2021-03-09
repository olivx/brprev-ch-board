
from boardgame.settings import BOARD_LENGTH


def test_board_length(board):
    assert len(board) == BOARD_LENGTH


def test_board_walk(board, player_impulsive):
    player_impulsive.position = 19
    assert board.walk(player_impulsive, 1) == 0


def test_board_check_winner(board, player_impulsive):
    for p in board.players:
        if player_impulsive != p:
            p.money = -1
    _player = board.check_winner(player_impulsive)
    board.winner = _player
    assert board.winner == player_impulsive
