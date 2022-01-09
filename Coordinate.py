import math
class Coordinate:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__ (self):
        return f"Coordinate: {self.x}, {self.y}"

    def __repr__ (self):
        return f"Coordinate: {self.x}, {self.y}"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __lt__(self, __o: object) -> bool:
        if self.y == __o.y:
            return self.x < __o.x
        return self.y < __o.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getDistance(self, coordinate):
        return math.abs(self.x - coordinate.x) + math.abs(self.y - coordinate.y)
    
    def isEqual(self, coordinate):
        return self.x == coordinate.getX() and self.y == coordinate.getY()
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, __o: object) -> bool:
        return self.isEqual(__o)