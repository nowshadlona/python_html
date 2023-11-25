# Group = input("Group: ")
# bangla1 = int(input("bangla1 mark: "))
# bangla2 = int(input("bangla2 mark: "))
# english1 = int(input("english1 mark: "))
# english2 = int(input("english2 mark: "))
# total_marks = bangla1 + bangla2 + english1 + english2
# print(total_marks)
# percentange = total_marks / 400 * 100
# print(percentange)

# print("---------students resultsheet--------")
# print("Group is: " + Group)
# print("togather marks are: 400")
# print("total marks are: " + str(total_marks))
# print("percentange is: " + str(percentange))

# if percentange >= 80:
#     print("Grade: A+")
#     print("grade points: 5")
# elif percentange >= 70:
#     print("Grade: B")
#     print("grade points: 4")
# elif percentange >= 60:
#     print("Grade: c")
#     print("grade points: 3")
# elif percentange >= 50:
#     print("Grade: D")
#     print("grade points: 2")
# else:
#     print("Greade: F (Fail)")
#     print("grade points: failure")

# name = "BANgLADESH"
# size = len(name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])
# print(name[8])
# print(name[9])
# print(name[0:4])
# print(name[4:10])
# print(name[4: ])
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.isupper())
# print(name[4].isupper())
# check_upper = name[0].isupper()
# if(check_upper):
#     print("the first letter is capital")
# else:
#     print("the first letter is not capital")
# txt = "i love apple, apple are my favourite fruit"
# x = txt.count("apple")
# print(x)

# for i in range(1,6):
#     print(i)
# for i in range(1,6,2):
#     print(i)

# name = "sam"
# print(name[0])
# for i in range(len(name)):
#     print(name[i])

# name = input("name: ")

# for char in name:
#     ascii = ord(char)
#     print(char + str(ascii))
    # print(str(ascii))
    # print(str(ascii), end=" ")
 
# 

# ch = input("name: ")
# print(ord(ch))

# name = input("name: ")
# for char in name:
#     ascii = ord(char)
#     print(char + str(ascii))

# l = [1,2,3,4,5]
# x = sum(l)
# print(x)

# Babu = [66,97,98,117]
# total = sum(Babu)
# print(total)

# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     sum = sum + asc
# print(sum)
# this is easy and perfect. given by teacher



# name = input("name: ")
# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     print(asc)
#     sum = sum + asc
# print(sum)
 
# letters = ["a", "b", "c", "d"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# print(combined)
# numbers = list(range(8))
# print(numbers)
# letters[0] = "A"
# print(letters)
# print(letters[0:2])
# print(letters[:2])
# print(letters[:])
# print(letters[::2])
# print(letters[::-1])
# print(numbers[::2])
# letters.append("e")
# print(letters)
# letters.insert(0,"-")
# letters.insert(3,"-")
# print(letters)
# letters.pop("0")      #or we can change (1) or (2) and other number(only for integer)
# print(letters)
# letters.remove("b")   # only for string
# print(letters)
# del letters[0:2]       # with del we can remove multiple item
# print(letters)
# letters.clear()
# print(letters)
# print(letters.index("d"))

# print(letters.count("e"))      # if the list donot have the number then

# letters = ["a", "b", "c", "d"]
# letters_1 = ["e", "f", "g"]      @ it add one value with another value
# letters.extend(letters_1)
# print(letters)

# letters.reverse()
# print(letters)             #both way reverse possible
# print(letters[::-1])

# letters = ["d", "a", "c", "b"]
# nums = [5,1,3,4,2]
# letters.sort()
# nums.sort()
# print(letters)
# print(nums)
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# list_1 = [10,20,30,40,50,60]
# list_2 = ["abcd", "efgh"]

# for i in range(len(list_1)):    
#     print(i,list_1[i])
#     sum = 0
# for i in list_1:
#     sum = sum + i
# print(sum)

# for m in range(len(list_2)):
#     print(m,list_2[m])
# sum = 0
# for m in list_2:
#     sum = sum +len(m)
# print(sum)

# name = input("name: ")
# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     print(asc)
#     sum = sum + asc
# print(sum)
list_1 = ['ab', 'cd', 'ef']

as_ci = []
for i in list_1:
    sum = 0
    for j in i:
        asci = ord(j)
        sum = sum+asci
    as_ci.append(asci)
print(as_ci)


# name = input("name: ")
# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     print(asc)
#     sum = sum + asc
# # print(sum)

# name1 = input("name1: ")
# sum1 = 0
# for i in range(len(name1)):
#     asc = ord(name1[i])
#     print(asc)
#     sum1 = sum1 + asc
# # print(sum1)

# name2 = input("name2: ")
# sum2 = 0
# for i in range(len(name2)):
#     asc = ord(name2[i])
#     print(asc)
#     sum2 = sum2 + asc
# # print(sum2)
# list_1 = (sum,sum1,sum2)
# print(list_1)
name = "sam"