from time import time

def process_list(arr: list[int]) -> list[int]:
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_gen(arr: list[int]) -> list[int]:
    return [i ** 2 if i % 2 == 0 else i**3 for i in arr]


# Для вычисления process_list в среднем нужно 0,2116758108139038 секунды,
# в то время как для process_list_gen 0,20903518199920654 секунды, что на 1.358% быстрее, то есть в районе погрешности.
if __name__ == "__main__":
    arr = [i for i in range(10**6)]
    t1 = time()
    process_list(arr)
    t2 = time()
    process_list_gen(arr)
    t3 = time()
    print(f"Time to process_list(arr) = {t2 - t1}, time to process_list_gen(arr) = {t3 - t2}")
    # timeList = 0
    # timeListGen = 0
    # for i in range(10):
    #     t1 = time()
    #     process_list(arr)
    #     t2 = time()
    #     process_list_gen(arr)
    #     t3 = time()
    #     timeList += t2 - t1
    #     timeListGen += t3 - t2
    # print(timeList / 10, timeListGen / 10)