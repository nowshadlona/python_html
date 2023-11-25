
# name = input("name: ")
# for char in name:

#     ascii = ord(char)    
#     print(str(ascii))
    # print(char + str(ascii))
    # print(str(ascii), end=" ")

# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     sum = sum + asc
# print(sum)

# another opption
# name = "Babu"
# sum = 0
# for char in name:
#     print(char," - ascii value is",ord(char))
#     sum = sum + ord(char)
# print("total ascii value of",name,"is",sum)

#  this one give by the teacher

name = input("name: ")
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    print(asc)
    sum = sum + asc
print(sum)