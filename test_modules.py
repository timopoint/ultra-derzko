from modules import Greet, ADD, SUB, MUL, DIV

def test_Greet():
    assert Greet("TIM") == "Hello, dear TIM!"

def test_ADD():
    assert ADD(17, 13) == 30

def test_SUB():
    assert SUB(103, 63) == 40

def test_MUL():
    assert MUL(13, 5) == 65

def test_DIV():
    assert DIV(34, 17) == 2