# 1 - Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.

# def sorted_arr():
#     arr = []
#     for i in range(5):
#         element = int(input(f"Enter element {i + 1}: "))
#         arr.append(element)

#     ascending = sorted(arr)
#     descending = sorted(arr, reverse=True)

#     print("Original Array:", arr)
#     print("Array in Ascending Order:", ascending)
#     print("Array in Descending Order:", descending)

# sorted_arr()


# ============================================================================

# 2 - Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.

# def g_arr():
#     start = int(input("Enter the starting number: "))
#     length = int(input("Enter the length of the array: "))
    
#     arr = list(range(start , start + length))

#     print(arr)

# g_arr()

# ============================================================================

# 3 - Write a program which repeatedly reads numbers until the user
# 	    enters “done”. Once “done” is entered, print out the total, count, and average of the numbers.
# 	    If the user enters anything other than a number, detect their
#             mistake, print an error message and skip to the next number.

# def calc():
#     total = 0
#     count = 0
    
#     while True:
#         user_input = input("Enter a number (or type 'done' to finish): ")
        
#         if user_input == "done":
#             break
        
#         try:
#             number = float(user_input)
#             total += number
#             count += 1
#         except ValueError:
#             print("Error: Invalid input. Please enter a valid number.")
    
#     if count > 0:
#         average = total / count
#         print(f"Total: {total}")
#         print(f"Count: {count}")
#         print(f"Average: {average}")
#     else:
#         print("No valid numbers were entered.")

# calc()