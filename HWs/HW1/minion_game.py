s = input()
vowels = ['A','E','I','O','U']

substrings = set()

for i in range(len(s)):
    for j in range(i, len(s) + 1):
        substrings.add(s[i:j + 1])

kevin = 0
stuart = 0
for word in substrings:
    if word[0] in vowels:
        kevin += s.count(word)
    else:
        stuart += s.count(word)

print(f"Кевин {kevin}" if kevin > stuart else f"Стюарт {stuart}")