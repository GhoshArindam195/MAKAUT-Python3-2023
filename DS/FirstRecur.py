def display(s, e):
    if s>e:
        return
    else:
        print(s)    #1 2.... 10
        display(s+1, e)

display(1, 10)