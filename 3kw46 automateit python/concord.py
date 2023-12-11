# concord.py
# 2023-12-07
import sys

def test():
    f=open('a',"r")
    for li in f:
        print '='.join(li.split('\t'))
    f.close()

def test2(fil):
    a={}
    for li in open(fil):
        if a.get(li)==None:
            a[li]=0
        else:
            a[li]+=1
    for i in a:
        print("%s %d\n" % (i,a[i]))

def test3(f):
    a={}
    for li in f:
        w=li.rstrip()
        a[w]=0 if a.get(w)==None else a[w]+1
    # FIXME is this really the best way to sort the dict?
    b=sorted(a.items(), key=lambda x: x[1], reverse=True)
    for x in b:
        print('\t'.join(map(str,x)))
test3(sys.stdin)