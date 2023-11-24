from abc import ABC, abstractmethod

class Father(ABC):
    def name(self):
        print("My name is Mary.")

    def eat(self):
        print("I can eat")
    @abstractmethod    
    def work(self):
        print("I can work")


class Mother:
    def name(self):
        print("My name is Mary.")

    def eat(self):
        print("I can eat")
    def work(self):
        print("I can code")

class Daughter( Father, Mother):
    pass

daughter = Daughter()
daughter.work()
# Father.work(daughter)
# print(Daughter.mro())





