# d1={1 : "Arindam", 2 : "Anupam", 3 : "Shayan"}
# d2={"Arindam" : {'B': "Banana", 'L':"Rice", 'D':"Roti"}, "Anupam":{'B':"Chicken", 'L':"Milk", 'D':"Mango"}}
# print(d2["Anupam"]['B'])

# d2=d1.copy();
# print(d1.keys())
# print(d1.items())


car={
    "brand" : "Audi",
    "Model" : "Q6",
    "Year"  : 2019,
}

car.update({"Year":2021})
car.update({"Color":"Black"})
print(car)
