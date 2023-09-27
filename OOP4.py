# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except and print an 
# error message and skip to the next number.


def calculate_sum(num1, num2, ):
    return num1 + num2 

def calculate_count(num1, num2):
    return 2  # Since there are always two numbers in this case

def calculate_average(num1, num2):
    return (num1 + num2 ) / 2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = input("Enter a number: ")

if num3 == "done":
    result_sum = calculate_sum(num1, num2)
    result_count = calculate_count(num1, num2)
    result_average = calculate_average(num1, num2)
    print("Sum:", result_sum)
    print("Count:", result_count)
    print("Average:", result_average)
else:
    print("You didn't type 'done' to calculate the sum, count, and average.")

