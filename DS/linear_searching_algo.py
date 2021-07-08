list=[]

flag = input("Lets start with pressing 'Y' ")

while flag=='y' or flag=='Y':
    num=input("Enter element")
    list.append(num)
    flag = input("Press 'Y' to enter more. Press 'N' otherwise")

key = input("Enter your searching element")

i=0
ans=-1
for i in range(len(list)):
    if(list[i] == key):
        ans=i
        break
if ans==-1:
   print("Not found")
else:
    print("Found at ",ans+1," position")