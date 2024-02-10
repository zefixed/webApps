n = int(input())
matr1 = []
matr2 = []

for _ in range(n):
    matr1.append(list(map(int, input().split())))
    
for _ in range(n):
    matr2.append(list(map(int, input().split())))

resMatr = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        resMatr[i].append(sum([matr1[i][k] * matr2[k][j] for k in range(n)]))

res = ""
for i in range(n):
    res += " ".join(list(map(str, resMatr[i]))) + "\n"

print(res)
