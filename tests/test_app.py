from app import Greet, Sum, mul 

def test_Greet():
    assert Greet("BOB") == "hello, BOB!"

def test_Sum():
    assert Sum(1, 5) == 6

def test_mul():
    assert mul(5, 5) == 25
