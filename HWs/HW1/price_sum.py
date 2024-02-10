import csv

with open('products.csv', encoding = 'utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    adult, retiree, child = 0, 0, 0
    for row in spamreader:
        try:
            temp = list(map(float, row[0].split(",")[1:]))
            adult += temp[0]
            retiree += temp[1]
            child += temp[2]
        except Exception as e:
            pass

print(f"{round(adult, 2)} {round(retiree, 2)} {round(child, 2)}")