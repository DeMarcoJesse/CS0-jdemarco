"""
Module to test the Chess class. 
"""

from chess import Chess


def test__init__() -> None:
    """Test the __init__ method"""
    chess = Chess(1, 1, 2, 2, 2, 8)
    assert chess.king == 1
    assert chess.queen == 1
    assert chess.rooks == 2
    assert chess.bishops == 2
    assert chess.knights == 2
    assert chess.pawns == 8

# add two test function to __init__ method to test the attributes are correctly initialized

def test__init__2():
    chess = Chess(0, 0, 0, 0, 0, 0)
    assert chess.king == 0
    assert chess.queen == 0
    assert chess.rooks == 0
    assert chess.bishops == 0
    assert chess.knights == 0
    assert chess.pawns == 0


def test__init__3():
    chess = Chess(3, 6, 4, 1, 1, 0)
    assert chess.king == 3
    assert chess.queen == 6
    assert chess.rooks == 4
    assert chess.bishops == 1
    assert chess.knights == 1
    assert chess.pawns == 0


def test__str__() -> None:
    """Test the __str__ metho"""
    chess = Chess()
    assert str(chess) == '1 1 2 2 2 8'


# add two test function to __str__ method to test the string representation is correct

def test__str__2():
    chess = Chess(0, 0, 0, 0, 0, 0)
    assert str(chess) == '0 0 0 0 0 0'


def test__str__3():
    chess = Chess(5, 4, 3, 2, 1, 0)
    assert str(chess) == '5 4 3 2 1 0'



def test__diff__():
    """Test the __sub__ method"""
    chess1 = Chess(1, 1, 2, 2, 2, 8)
    chess2 = Chess(0, 1, 1, 2, 1, 8)
    chess3 = chess1 - chess2
    assert chess3.king == 1
    assert chess3.queen == 0
    assert chess3.rooks == 1
    assert chess3.bishops == 0
    assert chess3.knights == 1
    assert chess3.pawns == 0


# add two test function to __sub__ method to test the difference is correct

def test__diff__2():
    chess1 = Chess(2, 2, 2, 2, 2, 2)
    chess2 = Chess(1, 1, 1, 1, 1, 1)
    chess3 = chess1 - chess2

    assert chess3.king == 1
    assert chess3.queen == 1
    assert chess3.rooks == 1
    assert chess3.bishops == 1
    assert chess3.knights == 1
    assert chess3.pawns == 1


def test__diff__3():
    chess1 = Chess(3, 3, 3, 3, 3, 3)
    chess2 = Chess(1, 2, 1, 2, 1, 2)
    chess3 = chess1 - chess2

    assert chess3.king == 2
    assert chess3.queen == 1
    assert chess3.rooks == 2
    assert chess3.bishops == 1
    assert chess3.knights == 2
    assert chess3.pawns == 1
    
