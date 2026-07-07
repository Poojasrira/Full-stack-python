# product_price = 5000
# delivery_charges = 100

# total = product_price + delivery_charges
# print(total)



# ###############
# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# student = 10
# groups = 2

# print(student // groups)

# ################################

# #followers = 100
# #followers += 1
# #print(followers)

# ################

# saved_password = "10"
# entered_password = "20"

# print(saved_password == entered_password)
# print(saved_password > entered_password)
# print(saved_password < entered_password)
# print(saved_password >= entered_password)
# print(saved_password <= entered_password)
# print(saved_password != entered_password)


# ################################################

# balance = 1500
# pin_correct = True
# if balance >= 1000 and pin_correct:
#     print("Withdraw allowed")
# else:
#     print("failed")


    #################

#product = input("Enter product name:")
#price = int(input("Enter product price:"))
#quantity = int(input("Enter quantity:"))
#total = price * quantity
#discount = total * 0.10
#final_bill = total - discount
#print("Product =",product)
#print("Total =",total)
#print("Discount =",discount)
#print("Final bill =",final_bill)

######################################

#password = input("Enter the password:")

#if password =="admin123":
#    print("welcome")

#else:
#    print("wrong password") 


#age = 15
#if age >= 18:
#    print("eligible to vote")
#else:
#    print("not eligible")

#marks = int(input("Enter the marks:"))
#if marks >=90:
#    print("10 cgpa")
#elif marks >=75:
#    print("8 cgpa")
#elif marks >=50:
#    print("7 cgpa")
#else:
#    print("fail")   


# ########################
# age = 25
# salary = 50000
# if age > 20 and salary >35000:
#     print("Loan Approved")
# ###############################

# ################################
# day = "sunday"
# if day == "monday" or day =="sunday":
#     print("holiday")
# ######################################

# ######################
# a = 20
# b = 30
# print(not(a == 30))
# #####################


# def withdraw_money():
#     pin = input("enter pin:")
#     if pin == "1234":
#         amount = int(input("enter amount:"))
#         balance = 10000
#         if amount <= balance:
#             balance = balance - amount
#             print("withdraw successful")
#             print("remaining balance:", balance)
#         else:
#             print("Insufficient balance")
#     else:
#         print("wrong pin")

# withdraw_money()


# for i in range(2,6):
#     print(i)

# users=["babu","ravi","arun"]
# for users in users:
#     print("message sent to", users)


# name = "dhoni"
# for ch in name:
#     print(ch)
##########################WHILE##########
# count =6
# while count >=5:
#     print(count)
#     count += 1


# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# password = ""
# while password != "1234":
#     password = input("enter password:")
#     print("login success")

student = ["ram","sam","arun"]
print(student)
student.append("alexa")
student.remove("sam")
print(student)