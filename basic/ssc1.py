# print("enter marks of subjects")
# bangla1 = int(input())
# bangla2 = int(input())
# english1 = int(input())
# english2 = int(input())
# total = bangla1+bangla2+english1+english2
# average = total/4

# if average>=90 and average <=100:
#     print("your grade is a+")
# elif average>=80 and average <=90:
#     print("your grade is a")
# elif average>=70 and average <=80:
#     print("your grade is a-")
# else:
#     ("invalid input")


Group = input("Enter Group: ")
bangla1 = int(input("Enter bangla1 mark: "))
bangla2 = int(input("Enter bangla2 mark: "))
english1 = int(input("Enter english1 mark: "))
english2 = int(input("Enter english2 mark: "))
total_marks = bangla1 + bangla2 + english1 + english2
print(total_marks)
percentange = total_marks / 400 * 100
print(percentange)

print("---------students resultsheet--------")
print("your Group is: " + Group)
print("togather marks are: 400")
print("total marks are: " + str(total_marks))
print("your percentange is: " + str(percentange))

if percentange >= 80:
    print("Grade: A+")
    print("grade points: 5")
elif percentange >= 70:
    print("Grade: B")
    print("grade points: 4")
elif percentange >= 60:
    print("Grade: c")
    print("grade points: 3")
elif percentange >= 50:
    print("Grade: D")
    print("grade points: 2")
else:
    print("Greade: F (Fail)")
    print("grade points: failure")

