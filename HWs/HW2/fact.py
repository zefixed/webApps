from time import time
from sys import setrecursionlimit, set_int_max_str_digits

setrecursionlimit(10**5 + 1)
set_int_max_str_digits(10**6)

def fact_rec(n: int) -> int:
    if n < 0: return 0
    elif n in [0, 1]: return 1
    else: return fact_rec(n - 1) * n
    

def fact_it(n: int) -> int:
    if n < 0: return 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Для вычисления факториала 100000 fact_rec в среднем тратит 3.464342784881592 секунды,
# в то время как fact_it 3.4185217142105104 секунды, что на 1.433% быстрее, то есть в районе погрешности.
if __name__ == "__main__":
    n = 100
    t1 = time()
    fact_rec(n)
    t2 = time()
    print(fact_it(n))
    t3 = time()
    print(f"Time to fact_rec({n}) = {t2 - t1}, time to fact_it({n}) = {t3 - t2}")
    
    # timeRec = 0
    # timeIt = 0
    # for i in range(10):
    #     t1 = time()
    #     fact_rec(n)
    #     t2 = time()
    #     fact_it(n)
    #     t3 = time()
    #     timeRec += t2 - t1
    #     timeIt += t3 - t2
    # print(timeRec / 10, timeIt / 10)