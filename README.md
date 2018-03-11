# Simulating robots
In this problem set you will practice designing a simulation and implementing a program that uses
classes.

### Simulation Overview ###
iRobot is a company (started by MIT alumni and faculty) that sells the [Roomba vacuuming robot](http://store.irobot.com/home/index.jsp) (watch
one of the product videos to see these robots in action). Roomba robots move about a floor, cleaning
the area they pass over. You will design a simulation to estimate how much time a group of
Roomba-like robots will take to clean the floor of a room. 

### Simulation Details ###
Here are additional details about the simulation model. Read these carefully.

* **Multiple robots**. In general, there are _N_ > 0 robots in the room, where _N_ is given. For
simplicity, assume that robots are points and can pass through each other or occupy the same
point without interfering.

* **The room**. The room is rectangular with some integer width _w_ and height _h_, which are given.
Initially the entire floor is dirty. A robot cannot pass through the walls of the room. A robot may
not move to a point outside the room.

* **Robot motion rules**:
  * Each robot has a position inside the room. We'll represent the position using coordinates
(x, y) which are real numbers satisfying 0 ≤ _x_ < _w_ and 0 ≤ _y_ < _h_. In our program we'll use
instances of the Position class to store these coordinates.
  * A robot has a direction of motion. We'll represent the direction using an integer _d_ satisfying
0 ≤ _d_ < 360, which gives an angle in degrees.
  * All robots move at the same speed _s_, which is given and is constant throughout the
simulation. Every time-step, a robot moves in its direction of motion by _s_ units.
  * When a robot hits a wall, it picks a new direction at random. The robot continues in that
direction until it reaches another wall.
* **Tiles**. You will need to keep track of which parts of the floor have been cleaned by the robot(s).
We will divide the area of the room into 1x1 tiles (there will be _w_ * _h_ such tiles). When a robot's
location is anywhere in a tile, we will consider the entire tile to be cleaned (as in the pictures
above). By convention, we will refer to the tiles using ordered pairs of integers: (0, 0), (0, 1), ...,
(0, _h_-1), (1, 0), (1, 1), ..., (_w_-1, _h_-1).
* **Termination**. The simulation ends when a specified fraction of the tiles in the room have been
cleaned.

If you find any places above where the specification of the simulation dynamics seems ambiguous, it is
up to you to make a reasonable decision about how your program/model will behave, and document
that decision in your code. 

### Part I: The `RectangularRoom` and `BaseRobot` classes ###
You will need to design two classes to keep track of which parts of the room have been cleaned as well
as the position and direction of each robot.
In **ps11.py**, we've provided skeletons for the following two classes, which you will fill in in Problem #1:
##### `RectangularRoom` #####
Represents the space to be cleaned and keeps track of which tiles have been cleaned.
##### `BaseRobot` #####
Stores the position and heading of a robot.
We've also provided a complete implementation of the following class:
Position
Stores the _x_- and _y_-coordinates of a robot in a room. 

#### Problem #1 ####
Complete the RectangularRoom and BaseRobot classes by implementing their methods
in **ps11.py** according to the given specifications. 

### Part II: Creating and using the simulator ###
#### Problem #2 ####
Each robot must also have some code that tells it how to move about a room, which will go in a
method called `updatePositionAndClean`.
Ordinarily we would consider putting all the robot's methods in a single class. However, later in
this problem set we'll consider robots with alternate movement strategies, to be implemented as
different classes with the same interface. These classes will have a different implementation of
`updatePositionAndClean` but are for the most part the same as the original robots. Therefore, we'd
like to use inheritance to reduce the amount of duplicated code.

We have already refactored the robot code for you into two classes: the `BaseRobot` class you
completed above (which contains general robot code), and a Robot class inheriting from it (which
contains its own movement strategy). 

#### Problem #3 ####
In this problem you will write code that runs a complete robot simulation.
In each trial, the objective is to gather data on how many time-steps are needed before a
specified fraction of the room has been cleaned. 

Implement the following function:
```Python
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.
    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    Visualization is turned on when boolean VISUALIZE is set to True.
 """
 ```
For your reference, here are some approximate room cleaning times. These times are with a robot
speed of 1.0.
* One robot takes around 150 clock ticks to completely clean a 5x5 room.
* One robot takes around 190 clock ticks to clean 75% of a 10x10 room.
* One robot takes around 310 clock ticks to clean 90% of a 10x10 room.
* One robot takes around 3250 clock ticks to completely clean a 20x20 room. 

(These are only intended as guidelines. Depending on the exact details of your implementation,
you may get times different from ours.) 

#### Visualizing robots ####
We've provided some code to generate animations of your robots as they go about cleaning a
room. These animations can also help you debug your simulation by helping you to visually
determine when things are going wrong. 
```Python
import ps11_visualize 
```

#### Problem #4 ####
Now, use your simulation to answer some questions about the robots' performance.
For the questions below, write code which will generate a plot using pylab. Put your
code inside the corresponding skeleton functions in **ps11.py** (showPlot1, showPlot2,
showPlot3, and showPlot4, respectively).

Each plot should have a title, descriptive labels on both axes, and a legend (if applicable). Assume
the robots are moving at a speed of 1.0.
1. How long does it take a single robot to clean 75% of each of the following types of rooms:
5x5, 10x10, 15x15, 20x20, 25x25? Output a figure that plots the mean time (on the Y-axis)
against the area of the room.
2. How long does it take to clean 75% of a 25x25 room with each of 1-10 robots? Output a
figure that plots the mean time (on the Y-axis) against the number of robots.
3. How long does it take two robots to clean 75% of rooms with dimensions 20x20, 25x16,
40x10, 50x8, 80x5, and 100x4? (Notice that the rooms have the same area.) Output a
figure that plots the mean time (on the Y-axis) against the ratio of width to height.
4. How does the time it takes to clean a 25x25 room vary as min_coverage changes? Output a
figure that plots mean time (on the Y-axis) against the percentage cleaned, for each of 1-5
robots. Your plot will have multiple curves.
Experiment with the number of trials. For your plots, use a number of trials which is large enough
that you think the output is reliable. 
