# 1- write a program that prints hello world

# print("Hello world")

# ==========================================================

#2- application to take a number in binary form from the user, and print it as a decimal

# binary_num=input("Please enter a binary Number: ")
# print (int(binary_num,2))

# ============================================================

#  3- write a function that takes a number as an argument and if the number
# 	divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 	divisible by both return "FizzBuzz" 


# def fizz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return number
    
# ============================================================

#4- Ask the user to enter the radius of a circle print its calculated area and circumference

# import math

# r = float(input ("Please enter the radius of the circle : "))
# area_of_circle = math.pi * (r**2)
# circumference_of_circle = 2*math.pi*r
# print("The area of circle is :" , area_of_circle)
# print("The circumference of circle is :" , circumference_of_circle)

# ============================================================

# 5- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

# name = input ("please enter your name")

# if name and name.isalpha :
#     email = input ("please enter your email")

#     print("\n Data provided :")
#     print(f"Name: {name}")
#     print(f"Email: {email}")

# else:
#     print("invalid name please try again")

# ============================================================

# 6- Write a program that prints the number of times the substring 'iti' occurs in a string

# string = input("Please enter a string")

# substring='iti'

# count = string.count(substring)

# print(f"The substring '{substring}' occurs {count} times .")