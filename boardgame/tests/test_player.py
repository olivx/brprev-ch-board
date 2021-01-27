from boardgame.models.base import House


def test_rent_or_bay_player_demanding_less_than_50(
    board, player_impulsive, player_demanding
):
    house = House(0, owner=player_impulsive)
    house.rent = 49
    house.price = 100
    player_demanding.rent_or_bay(house, board)
    assert player_demanding.money == 51


def test_bay_house_player_impulsive(board, player_impulsive, player_demanding):
    house = House(0, owner=None)
    house.price = 100
    player_impulsive.rent_or_bay(house)
    assert player_impulsive.money == 0
    assert player_impulsive.gameover == True


def test_rent_or_bay_player_demanding_less_than_50(
    board, player_impulsive, player_demanding
):
    house = House(0, owner=None)
    house.rent = 40
    house.price = 100
    player_demanding.rent_or_bay(house, board)
    assert player_demanding.money == 100


def test_rent_or_bay_player_demanding_more_than_50(
    board, player_impulsive, player_demanding
):
    house = House(0, owner=None)
    house.rent = 60
    house.price = 60
    player_demanding.rent_or_bay(house, board)
    assert player_demanding.money == 40


def test_rent_or_bay_player_player_cautious_cant_bay(
    board, player_impulsive, player_cautious
):
    house = House(0, owner=None)
    house.rent = 100
    house.price = 50
    player_cautious.rent_or_bay(house, board)
    assert player_cautious.money == 100


def test_rent_or_bay_player_player_cautious_can_bay(
    board, player_impulsive, player_cautious
):
    house = House(0, owner=None)
    house.rent = 100
    house.price = 20
    player_cautious.rent_or_bay(house, board)
    assert player_cautious.money == 80
