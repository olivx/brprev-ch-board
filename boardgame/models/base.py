from abc import ABC, abstractmethod
from collections import namedtuple
from datetime import datetime
from random import randint

from ..settings import BOARD_LENGTH, TIMEOUT


class House:

    def __init__(self, id, owner=None, *args, **kwargs):
        self.id = id
        self.owner = owner
        self.rent = randint(30, 120)
        self.price = randint(30, 120)

    def __repr__(self):
        return f"id:{self.id} owner:{self.owner} rent:{self.rent} price:{self.price}"

    def __str__(self):
        return f"id:{self.id} owner:{self.owner} rent:{self.rent} price:{self.price}"


class BasePlayer(ABC):
    STRATEGY = ("impulsive", "demanding", "cautious", "randomer")

    def __init__(self, strategy, position=0, money=100, *args, **kwargs):
        self.position = position
        self.money = money
        self.strategy = strategy
        self.gameover = False

    def __str__(self):
        return f"{self.strategy}"

    def __repr__(self):
        return f"{self.strategy}"

    def rent_or_bay(self, house, board=None):
        if house.owner:
            if self != house.owner:
                self.paid(house.rent, house.owner)
            return

        if self._roles_to_bay(house):
            house.owner = self


    # board[house.id] = house
    @abstractmethod
    def _roles_to_bay(self, house, board):
        raise NotImplementedError()

    def paid(self, price, owner=None):
        if owner == self:
            return

        self.money -= price
        if owner:
            owner.money += price
        if not self.money:
            self.gameover = True


class PlayerImpulsive(BasePlayer):

    def _roles_to_bay(self, house):
        self.paid(house.price, house.owner)
        return True


class PlayerDemanding(BasePlayer):

    def _roles_to_bay(self, house):
        if house.rent > 50:
            self.paid(house.price, house.owner)
            return True

        return False


class PlayerCautious(BasePlayer):

    def _roles_to_bay(self, house):
        if (self.money - house.price) >= 80:
            self.paid(house.price, house.owner)
            return True

        return False


class PlayerRandom(BasePlayer):

    def _roles_to_bay(self, house):
        if randint(0, 1) > 0:
            self.paid(house.price, house.owner)
            return True

        return False


class Board:

    def __init__(self, *args, **kwargs):
        self._winner = None
        self._played = 0
        self._players = []
        self.start_time = datetime.now()
        self._cards = [House(index, None) for index in range(BOARD_LENGTH)]

    @property
    def played(self):
        return self._played

    @played.setter
    def played(self, played):
        self._played = played

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winner):
        self._winner = winner

    @property
    def play_dice(self):
        return randint(1, 6)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, house):
        self._cards[position] = house

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"{self._cards}"

    def __repr__(self):
        return f"{self._cards}"

    def remove(self, player):
        for house in self._cards:
            if house.owner == player:
                house.owner = None
        self._players.remove(player)

    def walk(self, player, _dice=None):
        go_to_position = player.position + (_dice or self.play_dice)
        if go_to_position >= BOARD_LENGTH:
            player.money += 300
            go_to_position -= BOARD_LENGTH
        player.position = go_to_position
        return go_to_position

    def check_winner(self, player):
        if len(self.players) == 1:
            return player

        if TIMEOUT <= self.played:
            money = 0
            winner = None
            for _player in self._players:
                if _player.money > money:
                    money = _player.money
                    winner = _player
            return winner

        elements = [_player.money for _player in self._players if _player != player]
        if sum(elements) < 0:
            return player

        return None

    def play(self, player, board):
        if player.money <= 0:
            player.gameover = True
            return

        house = self._cards[self.walk(player)]
        player.rent_or_bay(house, board)

    def finish(self):
        return {
            "timeit": (datetime.now() - self.start_time).total_seconds(),
            "winner": self.winner,
            "money": self.winner.money,
            "played": self.played,
            "strategy": self.winner,
            "timeout": self.played > TIMEOUT,
        }
