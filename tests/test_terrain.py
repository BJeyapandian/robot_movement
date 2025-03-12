import unittest
from robot_movements.terrain import Terrain

class TestTerrain(unittest.TestCase):
    def setUp(self):
        
        self.terrain = Terrain(grid_size=10)

    def test_add_robot(self):
        
        self.terrain.add_robot(1)
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))

    def test_move_robot(self):
    
        self.terrain.add_robot(1)
        self.terrain.move_robot(1, "N3")
        self.assertEqual(self.terrain.get_robot_position(1), (0, 3))

    def test_robot_collision(self):
        
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)
        self.terrain.move_robot(1, "N4")  
        self.terrain.move_robot(2, "N5")  
        self.assertEqual(self.terrain.get_robot_position(2), (0, 3))

    def test_robot_boundary_stop(self):
        
        self.terrain.add_robot(1)
        self.terrain.move_robot(1, "N12")  
        self.assertEqual(self.terrain.get_robot_position(1), (0, 9))

    def test_invalid_robot_id(self):
        
        with self.assertLogs(level="ERROR") as log:
            self.terrain.move_robot(99, "E3")  
        self.assertIn("Error: Robot ID not found.", log.output[0])

if __name__ == "__main__":
    unittest.main()
