# var1 = "Hello world!"
# var2 = 4
# var3 = 36.7

# print(var1)
# print(type(var1))
# print(type(var2))
# print(type(var3))

#--Now different type of vars has diff type of operations---
# print(var2+var3)    #40.7
# print(var1+var2)    #error
# var4="Hi,"
# print(var4+var1)

var1="54"
var2="46"
# print(var1+var2)    #5446
# print(int(var1)+int(var2))  #100

# print(10*"Hello, world!\n")
# print(10*int(var1)+int(var2))  #540+46=586
print(10*str(int(var1)+int(var2)))  #100100100...100