from abc import ABC, abstractmethod


class Polygon(ABC):
    def noofsides(self):
        pass

class Triangle(Polygon):
     def noofsides(self):
        print("I have 3 sides.")

class Quadrilateral(Polygon):
     def noofsides(self):
        print("I have 4 sides.")


class Pentagon(Polygon):
     def noofsides(self):
        print("I have 5 sides.")


class Hexagon(Polygon):
     def noofsides(self):
        print("I have 6 sides.")    

hexagon = Hexagon()
pentagon = Pentagon()
triangle = Triangle()
q= Quadrilateral()

hexagon.noofsides()  

triangle.noofsides()

pentagon.noofsides()

q.noofsides()  







