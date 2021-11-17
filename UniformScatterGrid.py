import math

class UniformScatterGrid:

    def __init__(self, robots):
        self.robots = robots
        

    def findDimension(n):
        rc = math.ceil(math.sqrt(n))
        d = 2 * rc - 1
        return rc, d

    def findYmax(self, n):
        ymax = self.robots[0].coordinate.getY()
        for robot in self.robots:
            ymax = max(robot.coordinate.getY(), ymax)

        return ymax

    def findXmin(self, n):
        xmin = self.robots[0].coordinate.getX()
        for robot in self.robots:
            xmin = min(robot.coordinate.getX(), xmin)

        return xmin        
