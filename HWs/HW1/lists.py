n = int(input())
commands = []
for _ in range(n):
    commands.append(input())

lst = []
output = ""

if n < 1: print("")

for command in commands:
    command = command.split()
    match command[0]:
        case "insert":
            lst.insert(int(command[1]), int(command[2]))
        case "print":
            output += str(lst) + "\n"
        case "remove":
            lst.remove(int(command[1]))
        case "append":
            lst.append(int(command[1]))
        case "sort":
            lst.sort()
        case "pop":
            lst.pop()
        case "reverse":
            lst.reverse()
    
print(output)