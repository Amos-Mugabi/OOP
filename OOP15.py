# # Exception Handling.

# try:
#     fh = open("testfile", "w")
#     fh.write("This is my test file for exception handling")
# except IOError:
#      print("Error: cant find file or read data")
# else:
#     print("Written content in the file successfully")
# fh.close()



# num1 = int(input(("Enter a number:")))
# num2 = int(input(("Enter a number:")))

# try:
#     solution = num1 / num2
#     print("Please try again.")
# except ZeroDivisionError:
#     print("Error: cant find file or read data")
# except ValueError:
#     print("Written content in the file successfully")
    




class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
     raise Networkerror("Bad hostname")
except Networkerror as e:
     print(e.args)



        