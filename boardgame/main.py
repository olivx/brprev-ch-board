from datetime import datetime

from .models.base import Board
from .models.factory import create_board
from .settings import PLAYED_TIMES, TIMEOUT
from .utils import show_stats


def main():
    results = []
    for index in range(PLAYED_TIMES):
        board = create_board()
        while board.winner is None:
            for player in board.players:
                if player.gameover:
                    board.remove(player)
                winner = board.check_winner(player)
                if winner:
                    board.winner = winner
                    break

                board.play(player, board)
            board.played += 1
        results.append(board.finish())
    show_stats(results)


if __name__ == "__main__":
    main()
