import concurrent.futures
import time

def task(dur=1):
    print(f'sleeping for {dur} second(s)..')
    time.sleep(dur)
    return f'done sleeping {dur} seconds'

def test1():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(task,1)
        f2 = executor.submit(task,1)
        print(f1.result())
        print(f2.result())

def test2():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        res = [executor.submit(task,1) for _ in range(10)]
#       [print(r.result()) for r in res]
        for f in concurrent.futures.as_completed(res):
            print(f.result())

def test3():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        res = [executor.submit(task,s) for s in secs]
#       [print(r.result()) for r in res]
        for f in concurrent.futures.as_completed(res):
            print(f.result())

def test4():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        res = executor.map(task, secs)
        # executor will join all threads before returning

def test5():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        res = executor.map(task, secs)
        # executor will join all threads before returning

if __name__ == '__main__':

    start = time.perf_counter()
    test5()
    finish = time.perf_counter()

    print(f'finished in {round(finish-start,2)} second(s)')


