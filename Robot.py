from typing_extensions import final
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

    @staticmethod
    def isPositionEmpty(neighbours, coordinate):
        for robot in neighbours:
            if robot.coordinate.isEqual(coordinate):
                return False
        return True

    def FormGrid(self, n, gridFinal, yMax, xMin, neighbours):

        [rc, d] = gridFinal
        j = self.y - yMax
        finalCoordinate = Coordinate(self.x, self.y)

        # Case 1
        # Robot is <d rows away
        # Robot moves north. If blocked, moves eastward till a vacant north is found 
        if j <= d and j%2 == 0:
            while self.y == j:
                if Robot.isPositionEmpty(neighbours, finalCoordinate):
                    finalCoordinate.setY(finalCoordinate.getY()+1)
                    j-=1
                elif Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+1, finalCoordinate.getY())):
                    finalCoordinate.setX(finalCoordinate.getX()+1)
                else:
                    return -1
        
        # Case 2
        # Robot is >d rows away
        # Robot moves north. If blocked, moves east till north is vacant
        while j > d:
            if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()+1)):
                finalCoordinate.setY(finalCoordinate.getY()+1)
                j-=1
            elif Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+1, finalCoordinate.getY())):
                finalCoordinate.setX(finalCoordinate.getX()+1)
            else:
                return -1
        








         