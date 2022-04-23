#!/usr/bin/env python

"""
Unit tests for Primitive types
"""

from mtypes import PawnType
from primi import Pawn, Player


def test_pawn_1():
    """
    Pawn creation test
    :return: None
    """
    p = Pawn(PawnType.WHITE)
    assert p.ptype == PawnType.WHITE


def test_player_1():
    """
    Player creation test
    :return: None
    """
    p = Player("John Doe", PawnType.BLACK)
    assert len(p.pawns) == 9
    for i in range(0, 9):
        assert p.pawns[i].ptype == PawnType.BLACK
