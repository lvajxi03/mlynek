#!/usr/bin/env python

"""
Primitive types for mlynek
"""

from mlynek.mtypes import PawnType, BoardType


class Cell:
    """
    Place where you put the pawn(s)
    """
    def __init__(self, label: str):
        """
        Create cell instance
        """
        assert label is not None
        self.label = label
        self.neighbours = {
            'left': None,
            'right': None,
            'top': None,
            'bottom': None,
            'nw': None,
            'sw': None,
            'se': None,
            'ne': None
        }
        self.pawn = None

    def put(self, pawn):
        """
        Put a pawn on a cell
        :param pawn: Pawn to put on a cell
        :return: True if pawn is put here, False otherwise
        """
        assert pawn is not None
        if self.pawn:
            return False
        self.pawn = pawn
        return True

    def pop(self):
        """
        Pick the pawn from a cell
        :return: Pawn just picked up
        """
        pawn, self.pawn = self.pawn, None
        return pawn


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
        labels = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        board = Board(BoardType.THREE)
        for label in labels:
            cell = Cell(label)
            board.cells.append(cell)
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
