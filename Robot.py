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

    @staticmethod
    def isWestVacant(neighbours, coordinate, xMin):
        for x in range(xMin, coordinate.getX()):
            if Robot.isPositionEmpty(neighbours, Coordinate(x, coordinate.getY())):
                return True
        
        return False

    @staticmethod
    def isInAlternates(neighbours, coordinate, xMin):
        for robot in neighbours:
            if robot.coordinate.getY() == coordinate.getY() and (robot.coordinate.getX() - xMin)%2!=0:
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
            while True:
                if Robot.isPositionEmpty(neighbours, finalCoordinate):
                    finalCoordinate.setY(finalCoordinate.getY()+1)
                    j-=1
                    break

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
        
        # Case 3
        # Robot is not in Xmin and not in alternative rows
        # Robot moves west if west is empty else moves east or waits
        while finalCoordinate.getX() != xMin and (finalCoordinate.getY() - yMax) % 2 != 0:
            if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()-1, finalCoordinate.getY())) and Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()-2, finalCoordinate.getY())):
                finalCoordinate.setX(finalCoordinate.getX() - 1)
            elif not Robot.isWestVacant(neighbours, finalCoordinate, xMin):
                if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+1, finalCoordinate.getY())) and Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+2, finalCoordinate.getY())):
                    finalCoordinate.setX(finalCoordinate.getX() + 1)
            else:
                return -1

        # Case 4
        # Robot moves to odd row north if all nodes are in alternate and is in among first rc robots in row and target row above is empty
        while Robot.isInAlternates(neighbours, finalCoordinate, xMin) and finalCoordinate.getY() != yMax and finalCoordinate.getX() <= xMin + 2*(rc-1) and Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY() - 2)):
            finalCoordinate.setY(finalCoordinate.getY() - 2)







         