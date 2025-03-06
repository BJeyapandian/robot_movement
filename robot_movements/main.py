from robot_movements.terrain import Terrain

def main():
    terrain = Terrain()

    while True:
        print("\nOptions:\n1. Add Robot\n2. Move Robot\n3. Show Robot Position\n4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                robot_id = int(input("Enter Robot ID: ").strip())
                terrain.add_robot(robot_id)
            except ValueError:
                print("Error: Robot ID must be an integer.")

        elif choice == "2":
            try:
                robot_id = int(input("Enter Robot ID: ").strip())
                command = input("Enter move command (e.g., N3, E2): ").strip().upper()
                terrain.move_robot(robot_id, command)
            except ValueError:
                print("Error: Robot ID must be an integer.")

        elif choice == "3":
            try:
                robot_id = int(input("Enter Robot ID: ").strip())
                position = terrain.get_robot_position(robot_id)
                if position:
                    print(f"Robot {robot_id} is at position {position}.")
            except ValueError:
                print("Error: Robot ID must be an integer.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
