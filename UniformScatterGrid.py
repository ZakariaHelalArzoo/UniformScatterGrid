import random
import math
from Coordinate import Coordinate
from Robot import Robot
import Grid
class UniformScatterGrid:

    def __init__(self):
        self.n = 9
        self.robots = [] 

        for i in range(self.n):
            xCor = random.randint(0, Grid.WINDOW_WIDTH) // Grid.BLOCK_SIZE
            yCor = random.randint(0, Grid.WINDOW_HEIGHT) // Grid.BLOCK_SIZE
            self.robots.append(Robot(i, Coordinate(xCor, yCor)))

        
    @staticmethod
    def findDimension(n):
        rc = math.ceil(math.sqrt(n))
        d = 2 * rc - 1
        return rc, d

    def findYmax(self):
        ymax = self.robots[0].coordinate.getY()
        for robot in self.robots:
            ymax = max(robot.coordinate.getY(), ymax)

        return ymax

    def findXmin(self):
        xmin = self.robots[0].coordinate.getX()
        for robot in self.robots:
            xmin = min(robot.coordinate.getX(), xmin)

        return xmin        

    def executeCycle(self):
        xMin = self.findXmin()
        yMax = self.findYmax()
        gridFinal = UniformScatterGrid.findDimension(self.n)
        
        Grid.render(self.robots)

        while True:
            for robot in self.robots:
                neighbours = robot.look(self.robots)
                coordinates = robot.compute(self.n, gridFinal, xMin, yMax, neighbours)
                #TODO: Implement priority ordering of movement (w->e->s->n)
                #TODO: If tie, check priority.If priority same, make arbitrary choice
                if coordinates != -1:
                    robot.move(coordinates)
            Grid.render(self.robots)

if __name__ == "__main__":
   obj = UniformScatterGrid()
   obj.executeCycle()