class Polygon:
    width = 0
    height = 0

    def set_values (self,w,h):
        Polygon.width = w
        Polygon.height = h

class Rectangle(Polygon):
    def area (self):
        return self.width * self.height

class Triangle(Polygon):
    def area(self):
        return (self.width * self.height)/2
