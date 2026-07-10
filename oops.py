# class student:   # student is a class name
#     name = "arun" # name is a attribute
#     def study(self): #represent current object
#         print("arun is studying")
# s1 = student() #s1 is a object
# print(s1.name)
# s1.study() #study is a method


# class student:
#     def details(self):
#         print("had breakfast")
# s1 = student()
# s1.details()

# student.details(s1)


# class student:
#     def __init__(self, name,age): #init is a constructor
#         self.name = name
#         self.age = age
# s1 = student("arun",22)
# s2 = student("babu",23)
# s3 = student("janu",24)
# print(s1.name,s1.age, s2.name,s2.age, s3.name,s3.age)


# class bank:
#     def __init__(self,balance):
#         self.balance = balance
#     def check_balance(self):
#         print(self.balance)

# account = bank(5000)
# account.check_balance()

# class user:
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print(self.name,"loged in")

# u1=user("nibba") 
# u2=user("nibbi")
# u1.login(),u2.login()

###### single level inheritance########
# # Parent class
# class Father:
#     def house(self):
#         print("father has a house")

# # Child class
# class Son(Father):
#     def bike(self):
#         print("son has a bike")

# s = Son()

# s.house()
# s.bike()
#####################################

#########multilevel inheritance########
# class Grandfather:
#     def land(self):
#          print("grandfather has a land")

# class Father(Grandfather):
#     def house(self):
#          print("father's land")

# class Son(Father):
#     def car(self):
#          print("son has a car")

# obj = Son()

# obj.land()
# obj.house()
# obj.car()
##################################

############multiple level###########

# class appa:
#     def house(self):
#         print("appa's house")
# class amma:
#     def car(self):
#         print("amma's car")
# class maga(appa,amma):
#     def bike(self):
#         print("maga's bike")

# thirdclass = maga()
# thirdclass.house()
# thirdclass.car()
# thirdclass.bike()
########################################

#########hyrarical############
# class appa:
#     def house(self):
#         print("appa's house")
# class maga(appa):
#     def bike(self):
#         print("maga's bike")
# class daughter(appa):
#     def car(self):
#         print("daughter's car")

# m= maga()
# d = daughter()

# m.house()
# m.bike()

# d.house()
# d.car()
##################################

###########str()#####################used for redable object output############

# class student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
    
# s = student("king")
# print(s)
    
# def login(func):
#     def wrapper():
#         print("Checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("Dashboard page")
# dashboard()

# def message(func):
#     def wrapper():
#         print("Function started")
#         func()
#         print("Function ended")
#     return wrapper
# @message
# def hello():
#     print("Hello thannu")
# hello()

# @message
# def how():
#     print("How are you")
# how()

# @message
# def had():
#     print("Had lunch")
# had()

###########python to json#######
# import json

# student = {
#      "name":"babu",
#      "age":22

# }
# data = json.dumps(student)
# print(data)
###############################

#############json to python#########
# import json

# data = '{"name":"babu","age":23}'

# result  = json.loads(data)

# print(result["name"])
# print(result["age"])


# import requests
# response = requests.get(
#     "https://api.github.com/users/python"
# )

# data=response.json()
# print(data)