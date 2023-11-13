from __future__ import annotations

import json
from pprint import pprint

import pytest


def test_1():
    """Test pour comparer la génération avec le fichier simple"""
    quad = QuadTree
    test = QuadTree(False, True, False, True)
    quad = QuadTree.from_list(QuadTree.from_file("quadtree_easy.txt"))
    assert quad.__eq__(test) is True


def test_2():
    """Test pour comparer la génération avec le fichier complexe"""
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
    assert quad.__eq__(test) is True


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
        """TODO"""
        # ça ne marchait pas et ça cassait tout
        return 1
    
    @staticmethod
    def from_file(filename: str) -> list:
        """Ouverture et "formatage" du fichier"""
        data: list
        contenu: str
        contenu: str = open(filename, "r")
        data = json.load(contenu)
        return data
  
    @staticmethod
    def from_list(data: list, depth: int = 0) -> QuadTree:
        """ Generation du Quadtree à partir d'une liste (un collègue m'a un peu aidé, pour épurer un peu mon code) """
        depth = depth + 1
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
        """TODO"""
        self._depth = value
    
    def __eq__(self, other):
        """Pour la comparaison lors de mes tests"""
        if isinstance(other, QuadTree):
            return self.hd == other.hd and self.hg == other.hg and self.bg == other.bg and self.bd == other.bd
        else:
            return False


"""if isinstance(QuadTree, QuadTree):
        return self.hd == other.hd & self.hg == other.hg & self.bg == other.bg & self.bd == other.bd"""

"""class TkQuadTree(QuadTree):
    def paint(self):
        """""" TK representation of a Quadtree""""""
        pass
"""
