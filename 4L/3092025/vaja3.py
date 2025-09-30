def toBinary(x):
    stevilo = ""
    stack = []
    y = x
    while y != 0:
        if y%2!=0:
            stack.append(1)
        else:
            stack.append(0)

        y = y//2

    while stack:
        stevilo += str(stack.pop())

    return  stevilo

print(toBinary(13))