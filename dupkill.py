
# bash> IFS=$'\n';for i in $(sort dup.txt | uniq | grep -v '\\$'| sed 's#\\\\#/#g' | sed 's#^...##'); do echo $i;mkdir -p "_3/$(dirname $i)" ;touch "_3/$i";done


import os
import re

def test():
    for i in range(1000):
        f=open("x%d"%i,"w")
        f.close()

def test2():
    for i in range(100):
        if os.path.isfile("x%d"%i):
            os.remove("x%d"%i)

def test3():
    f=open("x/y")
    f.close()

def test4():
    if not os.path.exists("aaa/bbb"):
        os.makedirs("aaa/bbb")

def test5():
    a={}
    p1 = re.compile('\\$')
    f = open("dup.txt",'r',encoding='UTF8')
    for li in f:
        if li.endswith('\\'): continue
        a[li.strip()]=True
    print(len(a.keys()) )


def test6():
    f=open("dup.txt",'r', encoding='UTF8')
    a=[li.strip() for li in f.readlines()]  # discard trailing CR
 #   a2 =  [re.findall(r'.*(?=\\$)',li) for li in a]
#    a2=[p for p in a if re.match(r'(?!.*\\$)', p)]
    a2=[p for p in a if not p.endswith(r'\\')]  # discard dirs
#    a3=[p[2:] for p in a2]
    a3=[r'\\'.join(p.split(r'\\')[1:]) for p in a2] # discard drive prefix
#    a4=[os.path.dirname(p) for p in a3]
#    print(a3)
    for p in a3:
        print(p)
        x=p.split(r'\\')    # FIXME did you have problem using os.path.split?
        d=r'\\'.join(["_d"]+x[:-1])     # get dir name, prepend with _d\
#        print("d=%s, x=%s"%(d,x))
        if not os.path.exists(d):
            os.makedirs(d)
        nam=r'\\'.join(["_d"]+x)
#        print("%s %s,"%(d,nam),end="")
        open(nam,"w").close()       # FIXME not possible to create files with trailing period (apparently a windows problem!)

#    print(a4)
#    print(len(a4))

test6()
