from datetime import datetime

import pytest

from boardgame import utils


def test_show_results(capsys):
    results = [
        {
            "timeit": (
                datetime(2021, 10, 10) - datetime(2021, 10, 10, 10)
            ).total_seconds(
            ),
            "winner": 'impulsive',
            "money": 50,
            "played": 10,
            "strategy": 'impulsive',
            "timeout": True,
        }
    ]
    utils.show_stats(results)
    captured = capsys.readouterr()
    assert "Quantas partidas terminam por timeout: 1" in captured.out
    "Quantos turnos em média demora uma partida" in captured.out
    "Qual o comportamento que mais venceu: impulsive venceu: 1" in captured.out
    "Qual a porcentagem de vitórias por comportamento dos jogadores:" in captured.out
