from robot_movements.robot import Robot
import logging


logging.basicConfig(level=logging.INFO)  

class Terrain:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            logging.error("Error: Robot ID exists.")
            return
        self.robots[robot_id] = Robot(robot_id, self.grid_size)
        logging.info(f"Robot {robot_id} added at (0,0).")

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            logging.error("Error: Robot ID not found.")  
            return
        occupied_positions = {robot.get_position() for rid, robot in self.robots.items() if rid != robot_id}
        try:
            self.robots[robot_id].move(command, occupied_positions)
        except ValueError as e:
            logging.error(f"Error: {e}")  

    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            logging.error("Error: Robot ID not found.")  
            return None
        return self.robots[robot_id].get_position()
