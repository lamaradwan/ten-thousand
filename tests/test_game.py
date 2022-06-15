from ten_thousand.game import Game
from tests.flo import diff
import pytest


def test_no_for_play_game():
    game = Game()
    diffs = diff(game.play, 'version_2/quitter.sim.txt')
    assert not diffs, diffs


def test_one_and_done():
    game = Game()
    diffs = diff(game.play, 'version_2/one_and_done.sim.txt')
    assert not diffs, diffs


def test_bank_one_roll_then_quit():
    game = Game()
    diffs = diff(game.play, 'version_2/bank_one_roll_then_quit.sim.txt')
    assert not diffs, diffs

def test_repeate_roller():
    """Allow setting aside scoring dice and rolling the rest
        """
    diffs = diff(Game().play, path = 'tests/version_2/repeat_roller.sim.txt')
    assert not diffs, diffs
