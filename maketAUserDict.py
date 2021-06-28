d1={}
choice = input("Let's start with pressing Y: ")
while choice=='Y' or choice=='y':
    key=input("Enter your key: ")
    value = input("Enter your details: ")
    d1[key]=value
    choice=input("Do you want to enter more ? y/n ");

search_key=input("Enter your searching key: ")
if search_key in d1.keys():
    print(d1[key])
else:
    print("Sorry! Not Found.")