# mymath.py: random arithmetic puzzles
# 28.10.21 created
from random import randrange as rr
def test():
    op=('+','-','*','/')
    for i in range(0,10):
        eq='%d %c %d %c %d %c %d' %(rr(10), op[rr(4)], rr(10), op[rr(4)], rr(10), op[rr(4)], rr(10))
        # trap divide by 0
        try:
            print(eq,'=',eval(eq))
        except:
            None
    return None

test()
