def merge(mylist, l, m, h):
    i=0
    j=0
    k=0
    n1=m-l+1
    n2=h-m

    sublist1=[]
    sublist2=[]

    for i in range(n1):
        sublist1.append(mylist[l+i])
    for j in range(n2):
        sublist2.append(mylist[m+1+j])

    i = 0
    j = 0
    k = l

    while i<n1 and j<n2:
        if sublist1[i]<sublist2[j]:
            mylist[k]=sublist1[i]
            i+=1
        else:
            mylist[k]=sublist2[j]
            j+=1
        k+=1

    while i<n1:
        mylist[k] = sublist1[i]
        i += 1
        k += 1

    while j<n2:
        mylist[k] = sublist2[j]
        j += 1
        k += 1




def mergeSort(mylist, l, h):
    if l<h:
        m=(l+h)//2
        mergeSort(mylist, l, m)
        mergeSort(mylist, m+1, h)
        merge(mylist, l, m, h)



mylist=[]
len = int(input("Enter your size of the list"))

i = 0
for i in range (len):
    temp = int(input())
    mylist.append(temp)

print("Before Sorting.....")
for i in mylist:
    print(i, end=", ")

mergeSort(mylist, 0, len-1)

print("After Sorting.....")
for i in mylist:
    print(i, end=", ")
# print(mylist)
