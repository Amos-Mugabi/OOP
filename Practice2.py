
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = input("Enter a number: ")

def sum1(num1, num2):
    return (num1 + num2)

def count1(num1, num2):
    return 2

def average1(num1, num2):
    return (num1 + num2) / 2

if num3 == "done":
    sum2 = sum1(num1, num2)
    count2 = count1(num1, num2)
    average2 = average1(num1, num2)
# print("Sum: ", sum2)
print("Count:", count2)
print("Average:", average2)
    
    

