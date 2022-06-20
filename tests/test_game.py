from ten_thousand.game import Game
from tests.flo import diff
import pytest


def test_no_for_play_game():
    game = Game()
    diffs = diff(game.play, '../tests/version_2/quitter.sim.txt')
    assert not diffs, diffs


def test_one_and_done():
    game = Game()
    diffs = diff(game.play, '../tests/version_2/one_and_done.sim.txt')
    assert not diffs, diffs


def test_bank_one_roll_then_quit():
    game = Game()
    diffs = diff(game.play, '../tests/version_2/bank_one_roll_then_quit.sim.txt')
    assert not diffs, diffs


def test_repeat_roller():
    game = Game()
    diffs = diff(game.play, '../tests/version_2/repeat_roller.sim.txt')
    assert not diffs, diffs


def test_bank_first_for_two_rounds():
    game = Game()
    diffs = diff(game.play, '../tests/version_2/bank_first_for_two_rounds.sim.txt')
    assert not diffs, diffs


def test_hot_dices():
    game = Game()
    diffs = diff(game.play, '../tests/version_2/hot_dice.sim.txt')
    assert not diffs, diffs


def test_zilch():
    game = Game()
    diffs = diff(game.play, '../tests/version_3/zilcher.sim.txt')
    assert not diffs, diffs

def test_cheat():
    game = Game()
    diffs = diff(game.play, '../tests/version_3/cheat_and_fix.sim.txt')
    assert not diffs, diffs
