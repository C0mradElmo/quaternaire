from __future__ import annotations

import json
from pprint import pprint

import pytest


def test_1():
    quad = QuadTree
    test = QuadTree(False, True, False, True)
    quad = QuadTree.from_list(QuadTree.from_file("quadtree_easy.txt"))
    assert quad.hg & quad.hd & quad.bd & quad.bg == test.hg & test.hd & test.bd & test.bg


def test_2():
    aa = aa = QuadTree(True, False, False, False)
    a = a = QuadTree(False, False, False, aa)
    bb = QuadTree(False, True, False, False)
    b = QuadTree(False, False, bb, False)
    cc1 = QuadTree(True, False, False, True)
    cc2 = QuadTree(False, False, True, True)
    cc = QuadTree(cc1, cc2, False, False)
    c = QuadTree(False, False, False, cc)
    dd1 = QuadTree(False, False, True, True)
    dd2 = QuadTree(False, True, True, False)
    dd = QuadTree(dd1, dd2, False, False)
    d = QuadTree(False, False, dd, False)
    qt = QuadTree
    data = qt.from_file("quadtree.txt")
    test = QuadTree(a, b, c, d)
    quad = qt.from_list(data=data)
    pprint(quad.hg.depth)
    # assert quad.__eq__(test) == True
    assert quad.hg == test.hg

    """assert QuadTree.fromList(QuadTree.fromFile("quadtree.txt")) == [[0, 0, 0, [1, 0, 0, 0]], [0, 0, [0, 1, 0, 0], 0],
                                                                      [0, 0, 0, [[1, 0, 0, 1], [0, 0, 1, 1], 0, 0]],
                                                                      [0, 0, [[0, 0, 1, 1], [0, 1, 1, 0], 0, 0], 0]]"""


class QuadTree:
    NB_NODES: int = 4
    depth: int

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        """self.depth: int
        if issubclass(QuadTree, QuadTree):
            self.depth += 1"""
        return 1

    @staticmethod
    def from_file(filename: str) -> list:
        """ Open a given file, containing a textual representation of a list"""
        data: list
        contenu: str
        contenu: str = open(filename, "r")
        data = json.load(contenu)
        return data

    # @staticmethod
    # def fromList(data: list, self=None) -> QuadTree:
    #     """ Generates a Quadtree from a list representation"""
    #
    #     quad = QuadTree
    #     for i, value in enumerate(data):
    #         if not isinstance(data[i], list | tuple):
    #             data[i] = bool(data[i])
    #         else:
    #             data[i] = fromList(data[i])
    #             for j, value1 in enumerate(data):
    #                 if not isinstance(data[j], list | tuple):
    #                     data[j] = True if data[j] == 1 else False
    #                 else:
    #                     data[j] = QuadTree(data[j][0], data[j][1], data[j][2], data[j][3])
    #                     for k, value2 in enumerate(data):
    #                         if not isinstance(data[k], list | tuple):
    #                             data[k] = True if data[k] == 1 else False
    #                         else:
    #                             data[k] = QuadTree(data[k][0], data[k][1], data[k][2], data[k][3])
    #
    #     return quad(data[0], data[1], data[2], data[3])

    @staticmethod
    def from_list(data: list, depth: int = 0) -> QuadTree:
        depth = depth + 1
        """ Generates a Quadtree from a list representation"""
        new_data = []
        for child_node in data:
            if isinstance(child_node, list):
                new_data.append(QuadTree.from_list(data=child_node, depth=depth))
            else:
                new_data.append(bool(child_node))
        quad = QuadTree(*new_data)
        quad.depht = depth
        return quad


    @depth.setter
    def depth(self, value):
        self._depth = value

    def __eq__(self, other):
        if isinstance(other, QuadTree):
            return self.hd == other.hd and self.hg == other.hg and self.bg == other.bg and self.bd == other.bd
        return False

"""if isinstance(QuadTree, QuadTree):
        return self.hd == other.hd & self.hg == other.hg & self.bg == other.bg & self.bd == other.bd"""

"""class TkQuadTree(QuadTree):
    def paint(self):
        """""" TK representation of a Quadtree""""""
        pass
"""
