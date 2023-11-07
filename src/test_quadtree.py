
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

# from src import QuadTree, TkQuadTree
from src import QuadTree
def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.from_file()
    assert q.depth == 4

def test_single():
    filename = "quadtree_easy.txt"
    q = QuadTree.from_file()
    assert q.depth == 1