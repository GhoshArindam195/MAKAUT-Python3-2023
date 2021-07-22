# WAP program in python using recursion, where take a number input from the user print reverse order until it gets negative.

def printRev(n):
    if n<0:
        return
    else:
        print(n)
        printRev(n-1)


n = int(input("Enter your upper limit"))
printRev(n) #5