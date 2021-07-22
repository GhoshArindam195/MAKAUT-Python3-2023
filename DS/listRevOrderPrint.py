def printRev(mylist, s, len):
    if(s==len):
        return
    else:
        printRev(mylist, s+1, len)
        print(mylist[s])

len=int(input("Enter the size of your list"))
mylist=[]
i=0
print("Please insert",len," elements in sorted order")
for i in range(len):
    n=int(input())
    mylist.append(n)

printRev(mylist, 0, len)