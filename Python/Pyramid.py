inp = int(input("Enter a number..."))

# These helped a bit
# https://www.knowprogram.com/python/star-pattern-python-while-loop/,(pattern 5)
# https://www.youtube.com/watch?v=P-mCpH5f3js
# but I did not just copy/paste it

rows = 0
while rows < inp:
    space = inp - rows - 1
    while space > 0:
        print(end=" ")  # after a long time and many tutorials later,
        # this end=() function made it work somehow (I am not sure why yet)
        # (https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/)
        space = space - 1
    star = rows + 1
    while star > 0:
        print("*", end=" ")
        star = star - 1
    rows = rows + 1
    print()
