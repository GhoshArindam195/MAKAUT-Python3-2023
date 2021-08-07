myStack=[]
len = int(input("Enter your size of your stack"))
def push(n, top):
    if top==len-1:
        print("Stack Overflow")
    else:
        top+=1
        myStack=n[0]
    return top

def pop(top):
    if top==-1:
        print("Stack underflow")
    else:
        myStack[top]=-1
        top-=1
    return top;

def display(top):
    for i in range(0, top+1):
        print(top)
top=-1
print("Enter your elements")
for i in range(0, len):
    temp = int(input())
    top = push(temp, top)

display(top)

