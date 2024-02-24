import random
import math

def circle_square_mk(r: float, n: int) -> float:
    def count_pi(n):
        i, count = 0, 0
        while i < n:
            x, y = random.random(), random.random()
            if (x ** 2 + y ** 2) < 1:
                count += 1
            i += 1
        return 4 * (count / n)
    
    return round(count_pi(n) * r ** 2, 2)

'''
    Результаты при r=100
    Количество экспериментов: 10         circle_square_mk=28000.00   pi*r**2=31415.93   (Погрешность 10.87%)
    Количество экспериментов: 100        circle_square_mk=31600.00   pi*r**2=31415.93   (Погрешность 0.59%)
    Количество экспериментов: 1000       circle_square_mk=30880.00   pi*r**2=31415.93   (Погрешность 1.71%)
    Количество экспериментов: 10000      circle_square_mk=31472.00   pi*r**2=31415.93   (Погрешность 0.18%)
    Количество экспериментов: 100000     circle_square_mk=31391.20   pi*r**2=31415.93   (Погрешность 0.08%)
    Количество экспериментов: 1000000    circle_square_mk=31429.12   pi*r**2=31415.93   (Погрешность 0.04%)
    Количество экспериментов: 10000000   circle_square_mk=31419.81   pi*r**2=31415.93   (Погрешность 0.01%)
    Количество экспериментов: 100000000  circle_square_mk=31414.00   pi*r**2=31415.93   (Погрешность 0.01%)
    '''
if __name__ == "__main__":
    inp = input().split()
    r, n = float(inp[0]), int(inp[0])
    print(circle_square_mk(r, n))
    # r = 100
    # print(f"Результаты при r={r}")
    # for i in range(1, 10):
    #     funcRes = circle_square_mk(r, 10 ** i)
    #     formRes = math.pi * r ** 2
    #     print(f"Количество экспериментов: {10 ** i:<10} circle_square_mk={funcRes:<10.2f} pi*r**2={formRes:<10.2f} (Погрешность {abs(1 - funcRes / formRes) * 100:.2f}%)")