from __future__ import annotations

import json

import pytest


def test_1():
    quad = QuadTree
    test = QuadTree(False, True, False, True)
    quad = QuadTree.fromList(QuadTree.fromFile("quadtree_easy.txt"))
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
    quad = QuadTree
    test = QuadTree(a, b, c, d)
    quad = QuadTree.fromList(QuadTree.fromFile("quadtree.txt"))
    assert quad.hg & quad.hd & quad.bd & quad.bg == test.hg & test.hd & test.bd & test.bg

    """assert QuadTree.fromList(QuadTree.fromFile("quadtree.txt")) == [[0, 0, 0, [1, 0, 0, 0]], [0, 0, [0, 1, 0, 0], 0],
                                                                      [0, 0, 0, [[1, 0, 0, 1], [0, 0, 1, 1], 0, 0]],
                                                                      [0, 0, [[0, 0, 1, 1], [0, 1, 1, 0], 0, 0], 0]]"""


class QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.profondeur = 1
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg
        self.profondeur = self.depth

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        self.profondeur: int
        if issubclass(QuadTree, QuadTree):
            self.profondeur += 1
        return self.profondeur

    @staticmethod
    def fromFile(filename: str) -> list:
        """ Open a given file, containing a textual representation of a list"""
        data: list
        contenu: str
        contenu = open(filename, "r")
        data = json.load(contenu)
        return data

    @staticmethod
    def fromList(data: list, self=None) -> QuadTree:
        """ Generates a Quadtree from a list representation"""

        quad = QuadTree
        for i, value in enumerate(data):
            if not isinstance(data[i], list | tuple):
                data[i] = True if data[i] == 1 else False
            else:
                data[i] = QuadTree(data[i][0], data[i][1], data[i][2], data[i][3])

        return quad(data[0], data[1], data[2], data[3])


"""class TkQuadTree(QuadTree):
    def paint(self):
        """""" TK representation of a Quadtree""""""
        pass
"""
