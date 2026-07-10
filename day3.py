# student = ("ram", "sam", "bheem")
# print(student [-2])
# ##########tuple is a collection  used to store multiple variables, it is immutable (cannot be changed)##########

# numbers = (10,20,30,40)
# print(numbers)

# numbers = (20,30,40)
# print(numbers [2])

# data = (1,2,3)
# data[0] = 200
# print(data)


# x = (1,2,3,4,2)
# print(x.count(1))
# print(x.count(2))

# x = ("babu","sam","ram","sam")
# print(x.count("sam"))

# x = ("babu","sam","ram","sam")
# print(x.index("babu"))


# num = (10,20,30,40,50)
# print(num[1:4])

# num = (10,20,30,40,50)
# print(num[0:4])


#############################
####Set is a collection of :removing duplicate values and unorderd########

# x = {1,3,2,4,2,1,1}
# print(x)
# data = {1,2,3}
# data.remove(2)
# print(data)

# a = {1,2,3}
# b = {3,4,5}
# print(a|b)

# a = {1,2,3}
# b = {3,4,5}
# print(a & b)


#############function: reusable code#########
# def greeting():
#     print("hello students")
# greeting()

# def add():
#     return 10 + 20
# result = add()
# print(result)

# def sub():
#     return 10 - 20
# result = sub()
# print(result)

# def mul():
#     return 10 * 20
# result = mul()
# print(result)

# def div():
#     return 10/20
# result = div()
# print(result)

# def add(a,b):
#     print(a+b)
# add(10,20)


# def sub(a,b):
#     print(a-b)
# sub(10,20)


# def mul(a,b):
#     print(a*b)
# mul(10,20)


# def div(a,b):
#     print(a/b)
# div(10,20)


# def modulus(a,b):
#     print(a//b)
# modulus(10,20)

# add(10,20,30,40,50)
################*args#############
# def pooja(*numbers):
#     print(numbers)
# pooja(10,20,30,40,50,60)

# def add(*num):
#     total = 0
#     for i in num:
#         total += i
#     print(total)
# add(10,20,30,40,50,60)

##############**kwargs##############

# def student(**details):
#     print("name :",details["name"])
#     print("age :",details["age"])
#     print("job :",details["job"])
# student(
#     name="ram",
#     age=22,
#     job="sales",
# )


# def square(x):
#     return x * x
# print(square(16))

# square = lambda x:x*x
# print(square(25))


# square = lambda x:x*x*x
# print(square(25))

# add = lambda a,b:a+b
# print(add(20,30))

# x = 4
# if x >= 4:
#     print("Even")
# else:
#     print("Odd")

# even_odd= lambda x: "Even" if x % 2 == 0 else "Odd"
# print(even_odd(10))
# print(even_odd(15))

# pooja = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(pooja(20))
# print(pooja(17))
             
# check = lambda x: "Upper" if x.isupper else "Lower"
# print(check("HELLO"))
# print(check("hi"))

# ram = lambda name : name.upper()
# print(ram("hello world"))

# ram = lambda text : len(text)
# print(ram("hello world"))

# file = open("student.txt","w")
# file.write("hello ram")
# file.close()

# print("data written successfully")

# file = open("student.txt","r")
# data = file.read()
# print(data)
# file.close()

# file = open("student.txt","a")
# file.write("\nhow are you")
# file.close()

# print("Data appended successfully")

# file = open("student.txt", "r")
# print(file.read())
# file.close()

# try:
#     a = 10
#     b = 0
#     print(a/b)
# except:
#     print("something went wrong")

# try:
#     run = int(input("enter number:"))
#     print(num)
# except ValueError:
#     print("only number allowed")


# try:
#     a = int(input("enter A:"))
#     b = int(input("emter B:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter only numbers")


# try:
#     file = open("data.txt")
#     print(file.read())
# except:
#     print("file error")

# finally:
#     print("program completed")


# try:
#     print(10/2)
# except:
#     print("error")
# else:
#     print("success")






