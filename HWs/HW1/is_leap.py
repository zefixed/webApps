year = int(input())
if year % 100 == 0 and year % 400 == 0: print(True)
elif year % 100 != 0 and year % 4 == 0: print(True)
else: print(False)
