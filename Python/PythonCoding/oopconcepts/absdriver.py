from oopconcepts.rectangle import Rectangle
from oopconcepts.square import Square

sqobj = Square(10)
print(f'Area of Square : {sqobj.calculate_area()} \tPerimeter of Square : {sqobj.calculate_perimeter()}')


rectobj = Rectangle(10, 5)
print(f'Area of Rectangle : {rectobj.calculate_area()} \tPerimeter of Rectangle : {rectobj.calculate_perimeter()}')