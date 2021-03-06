# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 11:40:43 2017

@author: dmatt
"""

#creating a simulation

import math,random
import ps11_visualize
# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)
    #for debugging
    def __str__(self):
        #float values returned are huge, trancation required
        my_str = "(%1.1f,%1.1f)" %  (self.x,self.y)
        return my_str
# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        assert width > 0 and height > 0
        self.width = int(width)
        self.height = int(height)
        #cleaned_tiles will be as a fraction of the Room
        self.clean_tiles = {}

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        x,y = pos.getX(),pos.getY()
        clean_tile = (int(x),int(y))
        #mark it by storing it in cleaned_tiles
        self.clean_tiles[clean_tile] = (x,y)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        return (m,n) in self.clean_tiles

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return len(self.clean_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        x,y = random.uniform(0,self.width),random.uniform(0,self.height)
        return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        return 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        assert speed > 0
        self.speed = float(speed)
        self.room = room
        self.direction = random.randint(0,359)#random angle 0<=d<360
        self.position = self.room.getRandomPosition()

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.direction

    def setRobotPosition(self, new_position):
        """
        Set the position of the robot to new_position.

        position: a Position object.
        """
        # TODO: Your code goes here
        if type(new_position) is not Position:
            raise TypeError("Error at BaseRobot.setRobotPosition: new_position should be type Position")
        self.position = new_position

    def setRobotDirection(self, new_direction):
        """
        Set the direction of the robot to new_direction.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.direction = int(new_direction) % 360#just to be sure

class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here

        newPosition = self.position.getNewPosition(self.direction, self.speed)
        m,n = int(newPosition.getX()),int(newPosition.getY())
        #if the nextPosition is in the room
        if self.room.isPositionInRoom(newPosition):
            #go to that position/tile
            self.setRobotPosition(newPosition)
            # if the tile is not clean,clean it up
            if not self.room.isTileCleaned(m, n):
                self.room.cleanTileAtPosition(self.position)
        else:
            #if the next position is a wall, change angle
            self.setRobotDirection(random.randint(0,359))

# === Problem 3
def runTrial(num_robots,speed,width,height,min_coverage=100,robot_type=Robot):
    """We'll create robots in a room and see how they clean the room"""
    assert min_coverage in xrange(0,101)
    anim = Visualise.RobotVisualization(num_robots, width, height)
    #create a room
    Room1 = RectangularRoom(width,height)
    ##create a list of robots
    Robots = []
    for j in xrange(num_robots):
        Robots.append(robot_type(Room1,speed))
    house_cleaned = 0
    fraction_cleaned = []
    while house_cleaned < min_coverage:
        num_clean_tiles = Room1.getNumCleanedTiles()
        num_tiles = Room1.getNumTiles()
        house_cleaned = (num_clean_tiles * 100)/num_tiles
        fraction_cleaned.append(house_cleaned)
        for robot in Robots:
            robot.updatePositionAndClean()
        anim.update(Room1, Robots)
    #each member's spot in the list is the time it look to clean that fraction
    #of the room eg fraction_cleaned[10] is what fraction of the room was
    #cleaned after 10 time counts
    anim.done()
    return fraction_cleaned

def runSimulation(num_robots, speed, width, height, min_coverage, \
                  num_trials, robot_type=Robot, visualize=False):
    """ Runs NUM_TRIALS trials of the simulation and returns a list of lists,
    one per trial. The list for a trial has an element for each timestep of
    that trial, the value of which is the percentage of the room that is
    clean after that timestep. Each trial stops when MIN_COVERAGE of the
    room is clean. The simulation is run with NUM_ROBOTS robots of type
    ROBOT_TYPE, each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.
     Visualization is turned on when boolean VISUALIZE is set to True.
    """
    lst_trials = []
    for trial in xrange(num_trials):
        #append each trial to a list
        lst_trials.append(runTrial(num_robots,speed,width,height,min_coverage,robot_type))

    return lst_trials


runSimulation(5,2.0,20,20,100,3)
