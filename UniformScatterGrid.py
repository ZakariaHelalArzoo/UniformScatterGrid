import random
import math
import time
from collections import defaultdict

import pygame
import sys
from Coordinate import Coordinate
from Robot import Robot
import Grid
class UniformScatterGrid:

    def __init__(self):
        self.n = 75
        self.robots = [] 
        positions = set()
        for i in range(self.n):
            while True:
                xCor = random.randint(0, Grid.WINDOW_WIDTH) // Grid.BLOCK_SIZE
                yCor = random.randint(0, Grid.WINDOW_HEIGHT) // Grid.BLOCK_SIZE
                key = hash(Coordinate(xCor, yCor))
                if key in positions:
                    continue
                else:
                    self.robots.append(Robot(i, Coordinate(xCor, yCor)))
                    positions.add(key)
                    break

        # self.robots.append(Robot(0, Coordinate(0, 0)))
        # self.robots.append(Robot(1, Coordinate(1, 0)))
        # self.robots.append(Robot(2, Coordinate(2, 0)))
        # self.robots.append(Robot(3, Coordinate(0, 2)))
            

        
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
        for index, id in enumerate(ids):
            if self.robots[id].coordinate.getX() > new_coordinates[id].getX():
                priorities[index] = 4
            elif self.robots[id].coordinate.getX() < new_coordinates[id].getX():
                priorities[index] = 3
            elif self.robots[id].coordinate.getY() < new_coordinates[id].getY():
                priorities[index] = 2
            else:
                priorities[index] = 1

        return priorities

    def get_max_priority(self, ids, new_coordinates):
        movement_priorites = self.assignMovementPritority(ids ,new_coordinates)
        
        max_priority_id_index = 0
        for index, _ in enumerate(ids):
            if movement_priorites[index] > movement_priorites[max_priority_id_index]:
                max_priority_id_index = index

        return ids[max_priority_id_index]

    @staticmethod
    def simulation_completed(coordinates, rc):
        coordinates.sort()
        #print(coordinates)
        print(len(coordinates))

        count = 0
        for i in range(0, len(coordinates)-1):
            if coordinates[i+1].getY() - coordinates[i].getY() == 2:
                count = 0
            elif coordinates[i+1].getX() - coordinates[i].getX() == 2 and coordinates[i+1].getY() == coordinates[i].getY():
                count+=1
            else:
                return False
            if count >= rc:
                return False
        return True
            

    def executeCycle(self):
        xMin = self.findXmin()
        yMax = self.findYmax()
        gridFinal = UniformScatterGrid.findDimension(self.n)

        print (xMin, ",", yMax)
        
        Grid.render(self.robots)

        print (self.robots)

        isFinished = False

        while not isFinished:
            new_coordinates = []
            isFinished = False
            positions = defaultdict(list)
            for robot in self.robots:
                coordinate = robot.coordinate
                if random.randint(0, 1):
                    neighbours = robot.look(self.robots)
                    coordinate = robot.compute(self.n, gridFinal, xMin, yMax, neighbours)

                    # if not robot.coordinate.isEqual(coordinate):
                    #     next_move = True

                new_coordinates.append(coordinate)
                
                positions[hash(coordinate)].append(robot.id)
                
            print("look compute done")
            
            for _, ids in positions.items():
                print(ids)
                max_priority_id = self.get_max_priority(ids, new_coordinates)
                self.robots[max_priority_id].move(new_coordinates[max_priority_id])

            Grid.render(self.robots)

            print (self.robots)
            isFinished = UniformScatterGrid.simulation_completed(new_coordinates, gridFinal[0])

if __name__ == "__main__":

    for i in range(10):
        obj = UniformScatterGrid()
        obj.executeCycle()
        print("Finished ", i)
    while True:
        continue
