n = int(input("How many numbers you want to insert?"))
i=0
mylist=[]
#for(int i=0; i<n; i++)
for i in range (n):
    temp=int(input("Enter element"))
    mylist.insert(i, temp)
# print(mylist)

target=int(input("Enter your target"))

count=0
for x in mylist:
     if x==target:
         count +=1
print("your "+str(target)+" was occurred "+str(count)+" times")

