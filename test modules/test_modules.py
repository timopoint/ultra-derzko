from modules import Greet, ADD, SUB, MUL, DIV

def TEST_Greet():
    assert Greet("TIM") == "Hello, dear TIM!"

def TEST_ADD():
    assert ADD(17, 13) == 30

def TEST_SUB():
    assert SUB(103, 63) == 40

def TEST_MUL():
    assert MUL(13, 5) == 65

def TEST_DIV():
    assert DIV(34, 7) == 2