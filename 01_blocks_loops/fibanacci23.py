a, b = 0, 1                 # multiple assignment:
while a < 1000:
    # print(a)
    print(a, end='__')          ## dont print in new line
    a, b = b, a+b