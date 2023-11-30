arr = []

def process(command):
    global arr

    if command.startswith("insert"):
        _, index, value = command.split()
        arr.insert(int(index), int(value))
    elif command.startswith("print"):
        print(arr)
    elif command.startswith("remove"):
        _, value = command.split()
        arr.remove(int(value))
    elif command.startswith("append"):
        _, value = command.split()
        arr.append(int(value))
    elif command.startswith("sort"):
        arr.sort()
    elif command.startswith("pop"):
        arr.pop()
    elif command.startswith("reverse"):
        arr.reverse()
    else:
        print("Invalid command.")

def execute():
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            break
        process(command)

execute()

"""
Enter a command: insert 0 5
Enter a command: insert 1 10
Enter a command: insert 0 6
Enter a command: print
[6, 5, 10]
Enter a command: remove 6
Enter a command: append 9
Enter a command: append 1
Enter a command: sort
Enter a command: print
[1, 5, 9, 10]
Enter a command: pop
Enter a command: print
[1, 5, 9]
Enter a command: reverse
Enter a command: print
[9, 5, 1]
Enter a command: exit
"""