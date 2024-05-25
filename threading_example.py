import multiprocessing
import time

def task(dur=1):
    print(f'sleeping for {dur} second(s)..')
    time.sleep(dur)
    print('done sleeping')
    pass

def test1():
    task()
    task()
    pass

def test2():
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    pass

def test3():
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    pass

def test4():
    tlist=[]
    for _ in range(10):
        t = multiprocessing.Process(target=task)
        t.start()
        tlist.append(t)
    for t in tlist:
        t.join()
    pass

def test5(dur):
    tlist=[]
    for _ in range(10):
        t = multiprocessing.Process(target=task, args=[dur])
        t.start()
        tlist.append(t)
    for t in tlist:
        t.join()
    pass

if __name__ == '__main__':
    multiprocessing.freeze_support()

    start = time.perf_counter()
    test5(2.5)
    finish = time.perf_counter()

    print(f'finished in {round(finish-start,2)} second(s)')


