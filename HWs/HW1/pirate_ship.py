ship_capacity, cargo_count = list(map(int, input().split()))
cargoes = []

for cargo in range(cargo_count):
    inp = input().split()
    cargoes.append([inp[0], int(inp[1]), int(inp[2])])

for i in range(cargo_count):
    cargoes[i].append(cargoes[i][2] / cargoes[i][1])

cargoes = sorted(cargoes, key=lambda x: x[3], reverse=True)

res = ""

for cargo in cargoes:
    if ship_capacity - cargo[1] > 0:
        res += " ".join(list(map(str, cargo[:-1]))) + "\n"
        ship_capacity -= cargo[1]
    else:
        res += " ".join(list(map(str, [cargo[0], ship_capacity, round(cargo[2] - (cargo[1] - ship_capacity) * cargo[3], 2)]))) + "\n"
        break

print(res)