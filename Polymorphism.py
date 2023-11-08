
# Polymorphism

# Practical Task: 
# 1. Design a program to demonstrate inheritance
# 2. Read about polymorphism and design a simple hierarchy of related classes and demonstrate polymorphic behavior.

class Human():
                            # initiating the  object(move) for all classes.
    def move(self):
        print("I can walk.")
                            
class Male(Human):
     def move(self):
                            #  implementing it differently for other classes.
        print("I can run.")

class Baby(Human):
     def move(self):
        print("I can crawl.")

hum = Human()
male = Male()
bb = Baby()

                        # calling the objects.
hum.move()
male.move()
bb.move()


