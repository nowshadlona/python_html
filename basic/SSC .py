group = input("enter group: ")
bangla1 = int(input("enter bangla1 score: "))
bangla2 = int(input("enter bangla2 score: "))
english1 = int(input("enter english1 score: "))
english2 = int(input("enter english2 score: "))
overall_bangla = bangla1 + bangla2
overall_english = english1 +english2
general_math = int(input("enter general_math score: "))
higher_math_sub = int(input("enter higher_math_sub score: "))
higher_math_prac = int(input("enter higher_math_prac score: "))
higher_math = higher_math_sub + higher_math_prac
biology_sub = int(input("enter biology_sub score: "))
biology_prac = int(input("enter biology_prac score: "))
biology = biology_sub + biology_prac
physics_sub = int(input("enter physics_sub score: "))
physics_prac = int(input("enter physics_prac score: "))
physics = physics_sub + physics_prac
chemistry_sub = int(input("enter chemistry_sub score: "))
chemistry_prac = int(input("enter chemistry_prac score: "))
chemistry = chemistry_sub + chemistry_prac
islamic_religion = int(input("enter islamic_religion score: "))
social_science = int(input("enter social_science score: "))
ict = int(input("enter ict score: "))
total_scores = overall_bangla / 2 + overall_english / 2 + general_math + higher_math + biology + physics + chemistry + islamic_religion + social_science + ict
print(total_scores)
average_score = total_scores / 1000 * 100
print(average_score)

print("------SSC Resultsheet--------")
print("group is: " + group)
print("total marks are: 1000")
print("total scores are: " + str(total_scores))
print("average score is: " + str(average_score))

if (average_score >= 80 and average_score <=100):
    print ("grade: A+")
    print ("grade points: 5")
elif (average_score >= 70 and average_score <=79):
    print ("grade: A")
    print ("grade points: 4")
elif (average_score >= 60 and average_score <=69):
    print ("grade: A-")
    print ("grade points: 3.5")
elif (average_score >= 50 and average_score <=59):
    print ("grade: B")
    print ("grade points: 3")
elif (average_score >= 40 and average_score <=49):
    print ("grade: C")
    print ("grade points: 2")
elif (average_score >= 33 and average_score <=39):
    print ("grade: D")
    print ("grade points: 1")
elif (average_score >= 0 and average_score <=32):
    print ("grade: F")
    print ("grade points: 0")

