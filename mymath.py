# mymath.py: random arithmetic puzzles
# 28.10.21 created
from random import randrange as rr
def test():
    op=('+','-','*')
    for i in range(0,10):
        eq='%d %c %d %c %d %c %d' %(rr(10), op[rr(3)], rr(10), op[rr(3)], rr(10), op[rr(3)], rr(10))
        res=input('What is %s ? (<enter> to exit) ' %(eq))
        if res=='': break
        print('Correct' if abs(eval(eq)-int(res))<0.1 else 'Wrong, the correct answer is %d' %(eval(eq)))
    return None

test()