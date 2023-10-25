class Human:
    def __init__(self ):
        self.num_of_eyes = 2
        self.num_of_fingers = 10
    def name(self):
        print("My name is Mary.")

    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Female(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def work(self):
        super().work()
        print("I can code")
    def giveBirth(self):
        print("I can give birth.")
human = Human()
female = Female("Mary")
female.work()
human.name()
female.giveBirth()
# female.name()
print("I have ", female.num_of_eyes, "eyes.")





