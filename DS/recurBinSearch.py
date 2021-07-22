def binSearch(mylist, l, h, key):
    if l>h:
        return -1
    else:
        mid=(l+h)//2
        if key<mylist[mid]:
            return binSearch(mylist, l, mid-1, key)
        elif key>mylist[mid]:
            return binSearch(mylist,mid+1, h, key)
        elif key==mylist[mid]:
            return mid

len=int(input("Enter the size of your list"))
mylist=[]
i=0
print("Please insert",len," elements in sorted order")
for i in range(len):
    n=int(input())
    mylist.append(n)

k = int(input("Enter your searching key"))

found = binSearch(mylist, 0, len-1, k)

if found==-1:
    print("Not found")
else:
    print("found at ", found+1, " position" )