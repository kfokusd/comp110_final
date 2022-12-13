import math

# Final Exam - Question#2 (7 pts)
# - Implement 3 classes, Rectangle, Square, and Ellipse in FE_2.py
# - In FE_2.py, it has "TODO" comment, which require you to complete it
# - Detailed description of each class is in FE_2.py
# - Expected output is also defined as comment in FE_2.py
# - Please submit ONLY FE_2.py

##
## Shape Class
## - Please do NOT change this class
##
class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        pass

    def getPerimeter(self):
        return 0
    
    def getArea(self):
        return 0
    
    def __str__(self):
        return "Shape  ({:.2f}, {:.2f})".format(self._x, self._y)


##
## Circle Class
## - Please do NOT change this class
##
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self._radius = radius
    
    def getPerimeter(self):
        return (2.0 * math.pi * self._radius)
    
    def getArea(self):
        return (math.pi * self._radius * self._radius)

    def __str__(self):
        return "Circle  ({:.2f}, {:.2f}):  Radius={:.2f} with Area={:.2f} and Perimeter={:.2f}".format(self._x, self._y, self._radius, self.getArea(), self.getPerimeter())

##
## Rectangle Class
## - Inherits from Shape class
## - Rectange has width and length
## - If you don't know how to compute perimeter and area of a rectangle, please search on the Internet
##
## TODO: Implement Rectangle class


##
## Square Class
## - Inherits from Shape class
## - Square has length
## - If you don't know how to compute perimeter and area of a square, please search on the Internet
##
## TODO: Implement Square class


##
## Ellipse Class
## - Inherits from Shape class
## - Ellipse has xRadius and yRadius
## - Perimeter:
##   >> PI * ( 3(a+b) - SQRT( (3a+b)(a+3b) )), where a > b and a & b refer to radius of ellipse (xRadius, yRadius)
##   >> Hint: You need to use conditional statements to figure out which (xRadius or yRadius) is "a", and which (xRadius or yRadius) is "b"
## - Area: 
##   >> PI * xRadius * yRadius
##
## TODO: Implement Ellipse class


##
## Main
## Please do NOT change the following code.
## You MUST implement the above 3 classes, Rectangle, Ellipse and Square, in order to run this code without error
## 
fp = open("FE_2_input.txt")
ShapeList = []
for line in fp:
    fields = line.split(",")
    if ( fields[0] == '1' ):
        # ID=1 refers to Circle
        ShapeList.append(Circle(float(fields[1]), float(fields[2]), float(fields[3])))
    elif ( fields[0] == '2' ):
        # ID=2 refers to Rectangle
        ShapeList.append(Rectangle(float(fields[1]), float(fields[2]), float(fields[3]), float(fields[4])))
    elif ( fields[0] == '3' ):
        # ID=3 refers to Ellipse
        ShapeList.append(Ellipse(float(fields[1]), float(fields[2]), float(fields[3]), float(fields[4])))
    elif ( fields[0] == '4' ):
        # ID=4 refers to Square
        ShapeList.append(Square(float(fields[1]), float(fields[2]), float(fields[3])))

for shape in ShapeList:
    print(shape)


# Expected Output:
#Circle  (1.00, 1.00):  Radius=2.50 with Area=19.63 and Perimeter=15.71
#Rectangle  (2.00, 2.00):  Width=4.00 Length=6.00 with Area=24.00 and Perimeter=20.00
#Rectangle  (2.00, 3.00):  Width=6.00 Length=5.30 with Area=31.80 and Perimeter=22.60
#Circle  (0.00, 1.00):  Radius=5.50 with Area=95.03 and Perimeter=34.56
#Rectangle  (3.00, 0.00):  Width=4.00 Length=3.00 with Area=12.00 and Perimeter=14.00
#Ellipse  (0.00, 0.00):  xRadius=2.50 yRadius=2.50 with Area=19.63 and Perimeter=15.71
#Ellipse  (0.00, 0.00):  xRadius=3.00 yRadius=5.00 with Area=47.12 and Perimeter=25.53
#Circle  (0.00, 1.00):  Radius=10.00 with Area=314.16 and Perimeter=62.83
#Square  (0.00, 0.00):  Length=5.00 with Area=25.00 and Perimeter=20.00