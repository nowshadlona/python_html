# temperature = 35
# if temperature > 30:
#     print("it's warm")
#     print("drink water")
# print("done")
# temperature = 15
# if temperature > 30:
#     print("it's warm")
#     print("drink water")
# elif temperature > 20:
#     print("it's nice")
# else:
#     print("it's cold")
# print("done")
# name = "rafu"
# phone = "0171658312"
# if(len(name)==0 or len(phone)==0):
#     status = "failed"
#     print(status)
# else:
#     if(len(name)<6):
#         print("the name length must be minimum 6")
#     elif(len(phone)!=11):
#         print("phone number must be 11 digits")
#     else:
#         print("success")

name = "rafu"
phone = "01716583121"
if(len(name)==4 and len(phone)==11):
    status = "success"
    print(status)
else:
    if(len(name)>6):
        print("the name length must be minimum 4")
    elif(len(phone)!=10):
        print("phone number must be 11 digits")
    else:
        print("unsuccess")




