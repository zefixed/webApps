n = int(input())
iotime = []
for _ in range(n):
    iotime.append(list(map(int, input().split())))
time = int(input())
counter = 0
for i in iotime:
    if time in range(i[0], i[1] + 1):
        counter += 1

print(counter) 
