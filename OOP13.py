# #  Encapsulation


# class Employee:
#     def __init__(self, name, salary, project):
#         self.name = name
#         self.salary = salary
#         self.project = project
    


#     def work(self):
#         print("My name is ", self.name , "I am working on ", self.project)


#     def show(self):
#         print("My name is ", self.name , "I am working on ", self.project , "Project and  earning", self.salary )    


# em = Employee("Amos", "500k", "Software")
# em.show()
# em.work()

class Student():
    def __init__(self, name, age, reg_no):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age 

    def set_age(self, age):
        self.__age = age
        return self.__age
        
    def get_reg_no(self):
        return self.__reg_no 
        
    def set_reg_no(self, reg_no):
        if len(reg_no) <  10:
            print("Please enter your registration number")
        else:
            self.__reg_no = reg_no
            return self.__reg_no


    def Name(self):
        print("My name is", self.name)

st = Student("Mugabi", "20", "S22B23/011")
# st.get_age()
# print("My name is ", st.name )

st.Name()
st.set_age(30)
st.set_reg_no("S22B23/011")
print("I am ", st.get_age(), "years old.")

print("My registration number is ", st.get_reg_no(), ".")





