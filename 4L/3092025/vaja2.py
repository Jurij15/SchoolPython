def obrni(s):
    obrnjeno = ""
    stack = []

    for i in s:
        stack.append(i)

    while stack:
        obrnjeno += stack.pop()

    return obrnjeno

print(obrni("python"))