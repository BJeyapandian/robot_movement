class Robot:
    def __init__(self, robot_id, grid_size=10):
        self.robot_id = robot_id
        self.x, self.y = 0, 0
        self.grid_size = grid_size

    def get_position(self):
        return self.x, self.y

    def move(self, command, occupied_positions):
        if len(command) < 2 or command[0] not in "NESW" or not command[1:].isdigit():
            raise ValueError("Invalid command format! Use format like 'N3', 'E2'.")

        direction, steps = command[0], int(command[1:])
        dx, dy = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}[direction]

        for _ in range(steps):
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
                if (new_x, new_y) not in occupied_positions:
                    self.x, self.y = new_x, new_y
                else:
                    print(f"Collision at ({new_x}, {new_y})! Stopping.")
                    break
            else:
                print(f"Boundary at ({self.x}, {self.y})! Stopping.")
                break
