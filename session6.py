# student = {
#     "name":"amir",
#     "age":17,
#     "average":19.25,
#     "isProgrammer":True,
#     "programmingLanguages":["python","js"]
# }

# print(student["name"])
# print(student["average"])

# student["average"]=18.25
# print(student)

# student["schoolName"]="alghadir"
# print(student)

# print(student["fatherName"])
# get

# print(student.get("fatherName","key is not exist"))
# print(student.get("name","key is not exist"))

# del student["age"]
# print(student)

# print(student.items())

# for key,value in student.items():
#     print(f"{key}---> {value}")

# for item in student.items():
#     print(f"{item[0]} ---> {item[1]}")

# student.clear()
# print(student)

# print(student.keys())
# print(student.values())

# for key in student.keys():
#     print(f"{key} ---> {student[key]}")

# SET

# cars = {"benz","bmw","prado","pride","pride"}
# print(cars)
# for car in cars:
#     print(car)

# cars.add("405")
# print(cars)


# cars.remove("saina")
# print(cars)

# cars.discard("saina")
# print(cars)


cars = {"benz","bmw","prado","pride","pride"}
showRoomCars = {"405","saina","tiba","pride","bmw"}

# allCars = cars.union(showRoomCars)
# print(allCars)

# cars.update(showRoomCars)
# print(cars)

# sameCars = cars.intersection(showRoomCars)
# print(sameCars)

# cars.intersection_update(showRoomCars)
# print(cars)

symmetric = cars.symmetric_difference(showRoomCars)
print(symmetric)

cars.symmetric_difference_update(showRoomCars)
print(cars)
