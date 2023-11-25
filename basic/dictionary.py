# car = {"model":"m1", "color":"red", "price":"100"}
# print(car['model'])
# print(car['color'])
# print(car['price'])
# we can do both way (left side called keys and right side values)
# print(car.get('model'))
# if we want to look for the all keys
# print(car.keys())
# if we look for all values
# print(car.values())

# for i in car:             #keys
#     print(i)
# for i in car.values():     # all values
#     print(i)

# for i,j in car.items():       # all keys and values together
    # print(i,j)

# 2d dictionary
cars = {"car1":
         {"model":'m1',"price":100},
         "car2":
         {"model":'m2',"price":200}}
       
# for i,j in cars.items():
#     print(i,j)

# for i,j in cars.items():
#     for k in j.items():
#         print(i,k)

# cars["price"] = 300      #if wants to chage a specific value
# print(cars["price"])

# cars.update({"car1": "car1 is red"})     # if wants to upgrade keys
# print(cars["car1"])


# cars.pop("car1")      # for 2d dictionary if we want to delete one key and values
# print(cars)


# cars.popitem()      # if we want to remove the last item and if we do again then everything will be remove
# cars.popitem()
# print(cars)

# print(cars)       # if we want to copy the same key and values
# x = cars.copy()
# print(x)



