list_1 = ['ab', 'cd', 'ef']


name = input("name: ")
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    print(asc)
    sum = sum + asc
# print(sum)

name1 = input("name1: ")
sum1 = 0
for i in range(len(name1)):
    asc = ord(name1[i])
    print(asc)
    sum1 = sum1 + asc
# print(sum1)

name2 = input("name2: ")
sum2 = 0
for i in range(len(name2)):
    asc = ord(name2[i])
    print(asc)
    sum2 = sum2 + asc
# print(sum2)
list_1 = (sum,sum1,sum2)
print(list_1)