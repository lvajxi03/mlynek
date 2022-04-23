#!/usr/bin/env python

"""
Mlynek various types
"""

import enum


@enum.unique
class PawnType(enum.IntEnum):
    """
    Pawn type: are your pawns black or white?
    """
    WHITE = 0
    BLACK = 1


@enum.unique
class BoardType(enum.IntEnum):
    """
    Board type: 3, 6, 9 or 12 pawns
    """
    THREE = 0
    SIX = 1
    NINE = 2
    TWELVE = 3
