n = int(input())
data = []
for _ in range(n):
    data.append([input(), float(input())])

scores = set()

for iter in data:
    scores.add(iter[1])

mn2 = sorted(scores)[1]
names = []

for entry in data:
    if entry[1] == mn2:
        names.append(entry[0])

print("\n".join(sorted(names)))