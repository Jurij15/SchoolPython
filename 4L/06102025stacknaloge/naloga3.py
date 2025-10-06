def ReversePolishNotation(s):
    symbols = ["+","*","-"]
    stack = []
    syms = []

    for char in s:
        if char in symbols:
            syms.append(char)
        else:
            stack.append(char)
    return  stack+syms

print(ReversePolishNotation("A+B*C"))