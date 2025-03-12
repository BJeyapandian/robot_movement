import unittest
from robot_movements.terrain import Terrain

class TestTerrain(unittest.TestCase):
    def setUp(self):
        """Setup a terrain instance before each test."""
        self.terrain = Terrain(grid_size=10)

    def test_add_robot(self):
        """Test adding a robot to the terrain."""
        self.terrain.add_robot(1)
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))

    def test_move_robot(self):
        """Test if terrain correctly moves a robot."""
        self.terrain.add_robot(1)
        self.terrain.move_robot(1, "N3")
        self.assertEqual(self.terrain.get_robot_position(1), (0, 3))

    def test_robot_collision(self):
        """Test collision handling between two robots."""
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)
        self.terrain.move_robot(1, "N4")  # Move Robot 1 to (0,4)
        self.terrain.move_robot(2, "N5")  # Robot 2 should stop at (0,3) due to collision
        self.assertEqual(self.terrain.get_robot_position(2), (0, 3))

    def test_robot_boundary_stop(self):
        """Test if robot stops at boundary when terrain manages movement."""
        self.terrain.add_robot(1)
        self.terrain.move_robot(1, "N12")  # Should stop at (0,9)
        self.assertEqual(self.terrain.get_robot_position(1), (0, 9))

    def test_invalid_robot_id(self):
        """Test if moving a non-existent robot raises an error."""
        with self.assertLogs(level="ERROR") as log:
            self.terrain.move_robot(99, "E3")  # Robot ID 99 does not exist
        self.assertIn("Error: Robot ID not found.", log.output[0])

if __name__ == "__main__":
    unittest.main()
