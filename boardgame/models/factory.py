from ..models.base import (
    BasePlayer, Board, PlayerCautious, PlayerDemanding, PlayerImpulsive, PlayerRandom
)

strategies = {
    "impulsive": PlayerImpulsive,
    "demanding": PlayerDemanding,
    "cautious": PlayerCautious,
    "randomer": PlayerRandom,
}


def create_player(strategy: str, *args, **kwargs):
    try:
        return strategies[strategy](strategy=strategy, *args, **kwargs)

    except KeyError:
        available_strategies = ", ".join(strategies.keys())
        raise NotImplementedError(
            f"The player strategy '{strategy}' is not implemented."
            f"Please use the available strategies: {available_strategies}"
        )


def create_board():
    board = Board()
    players = [create_player(strategy) for strategy in BasePlayer.STRATEGY]
    board.players = players
    return board
