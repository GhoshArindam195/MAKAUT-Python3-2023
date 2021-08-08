def enqueue(myQueue, val):
    myQueue.append(val)

def dequeue(myQueue):
    myQueue.pop(0)

def display(myQueue, c):
    if c==leng:
        print("Queue is Empty")
    else:
        for i in range(0, leng-c):
            print(myQueue[i], end=" ")


myQueue=[]
leng = int(input("Enter your size: "))
print("Enter your elements: ")

c=0
for i in range(0, leng):
    temp = int(input())
    enqueue(myQueue, temp)

display(myQueue, c)

for i in range(0, leng):
    c+=1
    dequeue(myQueue)
print()
display(myQueue, c)