import unittest
from robot_movements.robot import Robot



class TestRobot(unittest.TestCase):
    def setUp(self):
        
        self.robot = Robot(robot_id=1, grid_size=10)

    def test_initial_position(self):
        
        self.assertEqual(self.robot.get_position(), (0, 0))

    def test_movement(self):
        
        self.robot.move("N3", set())  
        self.assertEqual(self.robot.get_position(), (0, 3))

    def test_diagonal_movement(self):
        
        self.robot.move("NE2", set())  
        self.assertEqual(self.robot.get_position(), (2, 2))

    def test_out_of_bounds(self):
        
        self.robot.move("N15", set())  
        self.assertEqual(self.robot.get_position(), (0, 9))  

    def test_collision_avoidance(self):
    
        occupied_positions = {(0, 2)}  
        self.robot.move("N3", occupied_positions)  
        self.assertEqual(self.robot.get_position(), (0, 1))  

    def test_invalid_command(self):
        
        with self.assertRaises(ValueError):
            self.robot.move("X3", set())  





if __name__ == "__main__":
    unittest.main()
