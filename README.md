# Robot Movement Simulation

## Overview
A Python project to simulate robots moving on a 10x10 grid. It prevents collisions and detects boundaries.

## Features
- Add robots to the grid
- Move robots in four directions
- Prevent out-of-bounds movement
- Collision detection

## Project Structure

robot_movement/

│── robot_movement/         
│   │── __init__.py         
│   │── robot.py            
│   │── terrain.py          
│   │── main.py             
│

│── tests/                  
│   │── __init__.py         
│   │── test_robot.py       
│   │── test_terrain.py  
│
│── requirements.txt        
│── README.md               
│── .gitignore    


## Run Project 
 Step 1 : Create the Project Structure like mention above.
 
 Step 2 : Run the main.py (CLI)
            - You should see a menu like:
               Options:
                 1. Add Robot
                 2. Move Robot
                 3. Show Robot Position
                 4. Exit
                 Enter your choice:

Step 3 : Select the options:
            Example Interaction:
              Enter your choice: 1
              Enter Robot ID: 1
              Robot 1 added at position (0,0).

              Enter your choice: 2
              Enter Robot ID to move: 1
              Enter move command (e.g., N3, E2): N3
              Robot 1 moved to (0,3).

              Enter your choice: 3
              Enter Robot ID: 1
              Robot 1 is at position (0,3).

              Enter your choice: 4
              Exiting...

## Run unit test:
Step 1 : Run all tests:

           python -m unittest discover tests
           
Step 2 : Run a specific test file:

           python -m unittest tests.test_robot
           
           python -m unittest tests.test_terrain


