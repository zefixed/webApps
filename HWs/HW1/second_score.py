n, scores = int(input()), input().split()
scores = map(int, scores)
print(sorted(list(set(scores)))[-2])