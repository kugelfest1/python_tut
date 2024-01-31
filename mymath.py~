# mymath.py: random arithmetic puzzles
# 28.10.21 created
from random import randrange as rr
def test():
    op=('+','-','*','//')
    for i in range(0,10):
        eq='%d %s %d %s %d %s %d' %(rr(10), op[rr(4)], rr(10), op[rr(4)], rr(10), op[rr(4)], rr(10))
        try:
          res=input('What is %s ? (-1 to exit) ' %(eq))
          if res=='-1': break
          print('Correct' if int(eval(eq))==int(res) else 'Wrong, the correct answer is %d' %(eval(eq)))
        except:
          print('Something went wrong, try again (-1 to exit)')
    return None

test()
