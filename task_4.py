commands = int(input())
list1 = []
for i in range(commands):
    com = input().split()
    if com[0] == "insert":
        list1.insert(int(com[1]), int(com[2]))
    elif com[0] == "print":
        print(list1)
    elif com[0] == "remove":
        list1.remove(int(com[1]))
    elif com[0] == "append":
        list1.append(int(com[1]))
    elif com[0] == "sort":
        list1.sort()
    elif com[0] == "pop":
        list1.pop()
    elif com[0] == "reverse":
        list1.reverse()
