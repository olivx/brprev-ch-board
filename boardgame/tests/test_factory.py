import pytest

from boardgame.models import factory


def test_strategies_key_error():
    with pytest.raises(NotImplementedError):
        factory.create_player('not-implemented')
