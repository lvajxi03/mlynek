#!/usr/bin/env python

"""
Primitive types for mlynek
"""

from mlynek.mtypes import PawnType, BoardType


class Cell:
    """
    Place where you put the pawn(s)
    """
    def __init__(self):
        """
        Create cell instance
        """
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.nw = None
        self.sw = None
        self.ne = None
        self.se = None


class Board:
    """
    Mlynek board
    """
    def __init__(self, btype: BoardType):
        """
        Create Board instance
        :param btype: board type
        """
        self.btype = btype
        self.cells = []

    @staticmethod
    def factory3():
        """
        Create board for three pawns, from factory
        :return: new board
        """
        board = Board(BoardType.THREE)
        board.cells = [Cell() for _ in range(0, 9)]
        return board

    @staticmethod
    def factory6():
        """
        Create board for six pawns, from factory
        :return: new board
        """
        board = Board(BoardType.SIX)
        board.cells = [Cell() for _ in range(0, 16)]
        return board

    @staticmethod
    def factory9():
        """
        Create board for nine pawns, from factory
        :return: new board
        """
        board = Board(BoardType.NINE)
        board.cells = [Cell() for _ in range(0, 24)]
        return board

    @staticmethod
    def factory12():
        """
        Create board for twelve pawns, from factory
        :return: new board
        """
        board = Board(BoardType.TWELVE)
        board.cells = [Cell() for _ in range(0, 24)]
        return board


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
        self.pawns = [Pawn(ptype) for _ in range(0, 9)]
