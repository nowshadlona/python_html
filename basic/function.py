# str1 = "lona"
# count = 0
# for i in str1:
#     count=count+1
# print(count) 

# def custom_len():
#     count = 0
#     for i in str1:
#         count=count+1
#     print(count)
# custom_len()

# def custom_len():
#     count = 0
#     for i in str1:
#         count=count+1
#     return count
# a = custom_len()
# print(a)

# x = len(str1)
# print(x)

# str1 = "lona"
# def custom_len(x):
#     count = 0
#     for i in x:
#         count=count+1
#     return count
# a = custom_len(str1)
# print(a)


# def custom_len(x,y):
#     count1 = 0
#     count2 = 0
#     for i in x:
#         count1=count1+1
#     for j in y:
#         count2=count2+1
#     return count1,count2

# str1 = "lona"
# str2 = "zarif"
# a,b = custom_len(str1,str2)
# print(a,b)

# when both str same len then we can use zip

def custom_len(x,y):
    count1 = 0
    count2 = 0
    for i,j in zip(x,y):
        count1=count1+1
        count2=count2+1
    return count1,count2

str1 = "lona"
str2 = "zari"
a,b = custom_len(str1,str2)
print(a,b)