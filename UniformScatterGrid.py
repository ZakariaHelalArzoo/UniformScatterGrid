import random
import math
import time
from collections import defaultdict
from Coordinate import Coordinate
from Robot import Robot
import Grid
class UniformScatterGrid:

    def __init__(self):
        self.n = 4
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
            ymax = min(robot.coordinate.getY(), ymax)

        return ymax

    def findXmin(self):
        xmin = self.robots[0].coordinate.getX()
        for robot in self.robots:
            xmin = min(robot.coordinate.getX(), xmin)

        return xmin       

    def assignMovementPritority(self, ids, new_coordinates):
        priorities = {}
        for id in ids:
            if self.robots[id].coordinate.getX() > new_coordinates[id].getX():
                priorities[id] = 4
            elif self.robots[id].coordinate.getX() < new_coordinates[id].getX():
                priorities[id] = 3
            elif self.robots[id].coordinate.getY() > new_coordinates[id].getY():
                priorities[id] = 2
            else:
                priorities[id] = 1

        return priorities

    def get_max_priority(self, ids, new_coordinates):
        #TODO: Implement priority ordering of movement (w->e->s->n)
        #TODO: If tie, check priority.If priority same, make arbitrary choice
        movement_priorites = self.assignMovementPritority(ids ,new_coordinates)
        
        max_priority_id = ids[0]
        for id in ids:
            if movement_priorites[id] > movement_priorites[max_priority_id]:
                max_priority_id = id

        return max_priority_id


    def executeCycle(self):
        xMin = self.findXmin()
        yMax = self.findYmax()
        gridFinal = UniformScatterGrid.findDimension(self.n)

        print (xMin, ",", yMax)
        
        Grid.render(self.robots)

        print (self.robots)

        next_move = True

        while next_move:
            new_coordinates = []
            next_move = False
            positions = defaultdict(list)

            for robot in self.robots:
                neighbours = robot.look(self.robots)
                coordinate = robot.compute(self.n, gridFinal, xMin, yMax, neighbours)

                if not robot.coordinate.isEqual(coordinate):
                    next_move = True

                new_coordinates.append(coordinate)
                
                positions[hash(coordinate)].append(robot.id)
                
            print("look compute done")

            for _, ids in positions.items():
                print(ids)
                max_priority_id = self.get_max_priority(ids, new_coordinates)
                self.robots[max_priority_id].move(new_coordinates[max_priority_id])

            Grid.render(self.robots)

            print (self.robots)


if __name__ == "__main__":
    obj = UniformScatterGrid()
    obj.executeCycle()
    print("Finished")
    while True:
        continue
