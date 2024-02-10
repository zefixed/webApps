n, m = list(map(int, input().split()))
given = list(map(int, input().split()))
up = list(map(int, input().split()))
down = list(map(int, input().split()))
happiness = 0

for num in given:
    if num in up: happiness += 1
    elif num in down: happiness -= 1

print(happiness)
