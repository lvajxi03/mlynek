#!/usr/bin/env python

"""
Mlynek varions types
"""

import enum

@enum.unique
class PawnType(enum.IntEnum):
    WHITE = 0
    BLACK = 1