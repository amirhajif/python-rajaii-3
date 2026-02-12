# score = int(input("please enter score: "))
'''
>10. ---> pass
ow.  ---> fail

indent
'''

# if score > 10:
#     if score <15:
#         print("GOOD")
#     else:
#         print("NICE")
# else:
#     print("fail")


# = va ==
# username = input("please enter username: ")
# if username == "admin":
#     print("admin welcome")
# else:
#     print("please signup")


# username = input("please enter username: ")
# if username != "admin":
#     print("please signup")
# else:
#     print("admin welcome")

'''
اگر بارسا ببرد یا مسی گل بزند علی شیرینی می دهم
در غیر اینصورت من شیرینی می دهد
'''


'''
username --> root
password --> root
'''

# username = input("please enter username: ")
# password = input("please enter password: ")

# if username=="root" and password=="root":
#     print("welcome")
# else:
#     print("please login")


'''
اگر بارسا ببرد من شام میدهم
در غیر اینصورت اگر بازی مساوی شود رضا شام می دهد
در غیراینصورت علی شام می دهد

'''

# seasson = int(input("please enter seasson number: "))
'''
1->bahar
2->tabestan 
,.....
'''

# if seasson==1:
#     print("bahar")
# elif seasson==2:
#     print("tabestan")
# elif seasson==3:
#     print("paiiz")
# elif seasson==4:
#     print("zemestan")
# else:
#     print("invalid")

# match seasson:
#     case 1:
#         print("bahar")
#     case 2:
#         print("tabestan")
#     case 3:
#         print("paiiz")
#     case 4:
#         print("zemestan")
#     case _:
#         print("invalid")


# username = input("please enter username: ")
# users = ["ali","ahmad","jafar"]

# if username in users:
#     print("valid user")
# else:
#     print("invalid user")

# if username not in users:
#     print("invalid user")
# else:
#     print("valid user")


# users = ["ali","ahmad","jafar"]

# if len(users)==0:
#     print("empty list")
# else:
#     print("contain items")

# if users:
#     print("contain items")
# else:
#     print("empty list")



# users = ["ali","ahmad","jafar"]
# print(users)

# for user in users:
#     print(f"welcome mr/mrs {user}")


scores = [10,8,20,12,16,9]


# sum=0

# for score in scores:
#     # sum = sum+score
#     sum+=score
    
# print(sum)

passCount,failCount = 0 , 0

# passCount=0
# failCount=0
for score in scores:
    if score>10:
        passCount = passCount+1
        # passCount+=1
    else:
        failCount = failCount+1
