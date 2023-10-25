st = 45978
while (st < 90000):
    print(st)
    x=st%100
    y=(st-x)//100
    st=x*1000+y