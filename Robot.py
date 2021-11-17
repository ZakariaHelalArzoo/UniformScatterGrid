import Coordinate
class Robot:
    def __init__(self, id) -> None:
        self.id = id
        self.coordinate = Coordinate()

    def __init__(self, id, coordinate) -> None:
        self.id = id
        self.coordinate = coordinate
    
    def setCoordinate(self, x, y):
        self.coordinate.setX(x)
        self.coordinate.setY(y)

    def look(self, robots):
        neighbours = []
        for robot in robots:
            if robot.id not in self.id:
                neighbours.append(robot)
        return neighbours

    def move(self, coordinate):
        self.coordinate.setX(coordinate.getX())
        self.coordinate.setY(coordinate.getY())

         