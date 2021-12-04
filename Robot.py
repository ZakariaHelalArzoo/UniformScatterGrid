from Coordinate import Coordinate
class Robot:
    def __init__(self, id) -> None:
        self.id = id
        self.coordinate = Coordinate()

    def __init__(self, id, coordinate) -> None:
        self.id = id
        self.coordinate = coordinate

    def __repr__ (self):
        return f"Robot: {self.id} {self.coordinate}"

    def look(self, robots):
        neighbours = []
        for robot in robots:
            if robot.id != self.id:
                neighbours.append(robot)
        return neighbours

    def compute(self, n, gridFinal, yMax, xMin, neighbours):
        return self.FormGrid(n, gridFinal, yMax, xMin, neighbours)

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
    def countRobotsToWest(neighbours, coordinate):
        count = 0
        for robot in neighbours:
            if robot.coordinate.getY() == coordinate.getY() and robot.coordinate.getX() < coordinate.getX():
                count += 1
        return count

    def FormGrid(self, n, gridFinal, xMin, yMax, neighbours):

        print ("In form grid for Robot:", self.id)

        [rc, d] = gridFinal
        j = self.coordinate.getY() - yMax
        finalCoordinate = Coordinate(self.coordinate.getX(), self.coordinate.getY())

        # Case 1
        # Robot is <d rows away
        # Robot moves north. If blocked, moves eastward till a vacant north is found 
        if j < d and j%2 == 1:
            print(f"{self.id} in case 1")
            while True:
                if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()-1)):
                    finalCoordinate.setY(finalCoordinate.getY() - 1)
                    return finalCoordinate

                elif Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+1, finalCoordinate.getY())):
                    finalCoordinate.setX(finalCoordinate.getX() + 1)

                else:
                    return self.coordinate

        print ("In form grid for Robot:", self.id, " Done 1")
        print (finalCoordinate)

        # Case 2
        # Robot is >d rows away
        # Robot moves north. If blocked, moves east till north is vacant

        moved_in_case_2 = False
        while j >= d:
            print(f"{self.id} in case 2")
            if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY() - 1)):
                finalCoordinate.setY(finalCoordinate.getY() - 1)
                j-=1
                moved_in_case_2 = True

            elif Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX() + 1, finalCoordinate.getY())):
                finalCoordinate.setX(finalCoordinate.getX() + 1)
                moved_in_case_2 = True

            else:
                return self.coordinate

        if moved_in_case_2:
            return finalCoordinate
        
        print ("In form grid for Robot:", self.id, " Done 2")
        print (finalCoordinate)

        # Case 3
        # Robot is not in Xmin and not in alternative nodes
        # Robot moves west if west is empty else moves east or waits
        # DONE: Doubt:- Robot moves arbitrary steps or single step in one cycle.
        moved_in_case_3 = False
        while finalCoordinate.getX() != xMin and (finalCoordinate.getY() - yMax) % 2 == 0:
            print(f"{self.id} in case 3")
            toWest = Robot.countRobotsToWest (neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()))
            if finalCoordinate.getX() == toWest*2 + xMin:
                break

            if finalCoordinate.getX() < ((toWest)*2 + xMin):
                if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+1, finalCoordinate.getY())) and Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()+2, finalCoordinate.getY())):
                    finalCoordinate.setX(finalCoordinate.getX() + 1)
                    moved_in_case_3 = True
                else:
                    return finalCoordinate

            elif Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()-1, finalCoordinate.getY())) and Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX()-2, finalCoordinate.getY())):
                finalCoordinate.setX(finalCoordinate.getX() - 1)
                moved_in_case_3 = True
            else:
                break

        if moved_in_case_3:
            return finalCoordinate

        print ("In form grid for Robot:", self.id, " Done 3")
        print (finalCoordinate)


        # # Case 4
        # # Robot moves to odd row north if all nodes are in alternate and is in among first rc robots in row and target row above is empty
        moved_in_case_4 = False
        while finalCoordinate.getY() != yMax and finalCoordinate.getX() <= xMin + 2*(rc-1) and Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY() - 2)):
            print (finalCoordinate)
            finalCoordinate.setY(finalCoordinate.getY() - 2)
            moved_in_case_4 = True

        if moved_in_case_4:
            return finalCoordinate

        print ("In form grid for Robot:", self.id, " Done 4")
        print (finalCoordinate)



        # # Case 5
        # #
        if j==0 and finalCoordinate.getX() > xMin + 2*(rc - 1):
            if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()+2)):
                while Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()+2)):
                    flag = False
                    finalCoordinate.setY(finalCoordinate.getY() + 2)
                    if Robot.countRobotsToWest(neighbours, finalCoordinate) < rc:
                        return finalCoordinate
            # else:
            #     return -1
        
        elif j>=1 and finalCoordinate.getX() > xMin + 2*(rc - 1):
            flag = False
            for row in range(yMax, finalCoordinate.getY(), 2):
                if Robot.countRobotsToWest(neighbours, Coordinate(finalCoordinate.getX(), row)) < rc:
                    flag = True
                    return finalCoordinate
            
            if flag:
                if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()-2)):
                    while Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()-2)):
                        finalCoordinate.setY(finalCoordinate.getY() - 2)
                        if Robot.countRobotsToWest(neighbours, finalCoordinate) < rc:
                            # #TODO:  make case 3 function and call here
                            # c3 = self.case3(xMin, yMax, neighbours, finalCoordinate)
                            # if c3 == -1:
                            #     return -1
                            # else:
                            #     finalCoordinate = c3
                            return finalCoordinate
                # else:
                #     return -1
            else:
                if Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()+2)):
                    while Robot.isPositionEmpty(neighbours, Coordinate(finalCoordinate.getX(), finalCoordinate.getY()+2)):
                        finalCoordinate.setY(finalCoordinate.getY() + 2)
                        if Robot.countRobotsToWest(neighbours, finalCoordinate) < rc:
                            return finalCoordinate
                # else:
                #     return -1

        print ("In form grid for Robot:", self.id, " Done 5")
        print (finalCoordinate)


        return finalCoordinate
