import unittest
from robot_movements.robot import Robot



class TestRobot(unittest.TestCase):
    def setUp(self):
        """Setup a robot instance before each test."""
        self.robot = Robot(robot_id=1, grid_size=10)

    def test_initial_position(self):
        """Test if robot starts at (0,0)."""
        self.assertEqual(self.robot.get_position(), (0, 0))

    def test_movement(self):
        """Test normal movement within bounds."""
        self.robot.move("N3", set())  # Move 3 steps north
        self.assertEqual(self.robot.get_position(), (0, 3))

    def test_diagonal_movement(self):
        """Test if the robot moves diagonally (NE)."""
        self.robot.move("NE2", set())  # Move northeast 2 steps
        self.assertEqual(self.robot.get_position(), (2, 2))

    def test_out_of_bounds(self):
        """Test if the robot stops at the grid boundary."""
        self.robot.move("N15", set())  # Try to move beyond grid
        self.assertEqual(self.robot.get_position(), (0, 9))  # Should stop at max limit

    def test_collision_avoidance(self):
        """Test if the robot stops when encountering an obstacle."""
        occupied_positions = {(0, 2)}  # Obstacle at (0,2)
        self.robot.move("N3", occupied_positions)  # Move towards (0,3)
        self.assertEqual(self.robot.get_position(), (0, 1))  # Stops before (0,2)

    def test_invalid_command(self):
        """Test if an invalid move command raises ValueError."""
        with self.assertRaises(ValueError):
            self.robot.move("X3", set())  # Invalid direction





if __name__ == "__main__":
    unittest.main()
