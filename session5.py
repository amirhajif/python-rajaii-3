# Loop in List - For
'''
range(0,10)
'''

# print(list(range(0,10)))

'''
10 bar hello ra chap konad
'''

# for i in range(0,10):
#     print("hello")

# get a number and show from 0 to number
# n=int(input("please enter number: "))
# # 12 --> 0 1 2 3 ... 12
# for i in range(0,n+1):
#     print(i)


# sum of even number before
# n=int(input("please enter number: "))

# way 1
# sum = 0
# for i in range(0,n+1):
#     if i%2==0:
#         sum+=i

# print(sum)

# way 2
# sum=0
# for i in range(0,n+1,2):
#     sum+=i
# print(sum)


# break
# continue

# for i in range(0,10):
#     if i==5:
#         break

#     print(i)

# print("end of loop")


# for i in range(0,10):
#     if i==5:
#         continue
#     print(i)

# print("end of loop")


'''
Loop
For
While
While tamam kar haye halgheh for ra support mikonad + option haye bishtari darad
Point:dar jahayii ke mishavad ba halgheh for code ra nevesht az for estefade shavad
'''

# for i in range(0,10):
#     print("hello")


# i=0
# while i<10:
#     print("hello")
#     i=i+1

'''
School
teacher input score
ta zamani ke moalem khast nomre vared kardan edame peyda kone
dar nahayat miangin nomarat neshan dade shavad
'''

# sum , count = 0 , 0
# while True:
#     score = int(input("please enter score: "))
#     sum+=score
#     count+=1
#     answare = input("do you want continue?y/n ")
#     if answare=='n':
#         break
# print(sum/count)

# Tuple
'''
Collection
1-List []
2-Tuple ()
3-Dictionary
4-set
'''

salaries = (1000,2000,3000)
print(type(salaries))

for salary in salaries:
    print(salary)
