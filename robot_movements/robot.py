class Robot:
    def __init__(self, robot_id, grid_size=10):
        self.robot_id = robot_id
        self.x, self.y = 0, 0
        self.grid_size = grid_size

    def get_position(self):
        return self.x, self.y

    def move(self, command, occupied_positions):
        valid_directions = ["N", "E", "S", "W", "NE", "NW", "SE", "SW"]

        # Extract direction and steps without regex
        for i in range(1, len(command)):
            if command[i].isdigit():
                direction, steps = command[:i], command[i:]
                break
        else:
            raise ValueError("Invalid command format! Use format like 'N3', 'E2', 'NE3', 'SW2'.")

        if direction not in valid_directions or not steps.isdigit():
            raise ValueError("Invalid direction or step count! Use N, E, S, W, NE, NW, SE, SW followed by a number.")

        steps = int(steps)

        # Compute movement based on conditions (instead of using a dictionary)
        dx, dy = 0, 0
        if "N" in direction:
            dy += 1
        if "S" in direction:
            dy -= 1
        if "E" in direction:
            dx += 1
        if "W" in direction:
            dx -= 1

        # Move step by step
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
