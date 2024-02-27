import pylab
import numpy as np

def initialize_grid(size):
    return np.ones((size, size), dtype=int)

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def Cproba(possible_moves, visited_counts):
    proba = [visited_counts[move] for move in possible_moves]
    total = sum(proba)
    return [prob / total for prob in proba]

def random_walk(grid_size, num_walkers):
    grid = initialize_grid(grid_size)
    visited_counts = initialize_grid(grid_size)
    visited = {i: set() for i in range(1, num_walkers + 1)}

    directions = [ (0, 1),  (0, -1), (1, 0), (-1, 0)  ]

    for walker in range(1, num_walkers + 1):
        curr_position = (0, 0)
        

        print(f"Walker {walker} started at position {curr_position}")

        while  curr_position != (5, 5):
            if 0 <= curr_position[0] < grid_size and 0 <= curr_position[1] < grid_size:
                visited[walker].add(curr_position)

                visited_counts[curr_position] += 1
                print(f"Walker {walker} walked to position {curr_position}")

            possible_moves = [
                (curr_position[0] + direction[0], curr_position[1] + direction[1])
                for direction in directions
            ]

            possible_moves = [
                move
                for move in possible_moves
                if 0 <= move[0] < grid_size and 0 <= move[1] < grid_size
                and move not in visited[walker]
            ]

            if not possible_moves:
                print("There are no possible moves")
                break

            probas = Cproba(possible_moves, visited_counts)
            chose = np.random.choice(len(possible_moves), p=probas)
            curr_position = possible_moves[chose]
            visited[walker].add(curr_position)
            

            # Display the grid using pylab
            pylab.imshow(visited_counts, cmap='hot', interpolation='nearest')
            pylab.pause(0.01)
            pylab.draw()

        if curr_position == (5, 5):
            print(f"Walker {walker} reached (5, 5)")
        else:
            print(f"Walker {walker} completed the walk")

    print("Final grid with walker counts:")
    print_grid(visited_counts)
    pylab.show()

if __name__ == "__main__":
    random_walk(20, 3)
