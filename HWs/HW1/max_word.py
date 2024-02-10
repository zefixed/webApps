with open('example.txt', encoding = 'utf-8', mode = 'r') as file: 
    text = file.read()

punctuations = ".,/|\\?!@#$%^&*«»()[]{};:\'\""

for punctuation in punctuations:
    text = text.replace(punctuation, "")

mx = [0, ""]
for word in text.split():
    if len(word) > mx[0]: mx = [len(word), word]

print(mx[1]) 