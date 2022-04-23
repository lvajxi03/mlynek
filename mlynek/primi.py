#!/usr/bin/env python

"""
Primitive types for mlynek
"""

from mtypes import PawnType


class Pawn:
    """
    Pawn abstraction
    """
    def __init__(self, ptype: PawnType):
        """
        Create Pawn instance
        :param ptype: Pawn type (white or black)
        """
        self.ptype = ptype


class Player:
    """
    Player abstraction
    """
    def __init__(self, nick: str, ptype: PawnType):
        """
        Create player instance
        :param nick: Player nickname
        :param ptype: type of pawns for player (white or black)
        """
        self.nick = nick
        self.ptype = ptype
        self.pawns = [Pawn(ptype) for i in range(0, 9)]

