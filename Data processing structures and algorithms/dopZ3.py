import numpy as np
from tqdm import tqdm

def is_valid_move(x, y, m, n, visited):
    """
    Checks if the move (x, y) is valid on an m x n chessboard
    and has not been visited before.
    """
    return 0 <= x < m and 0 <= y < n and visited[x][y] == 0

def find_knight_route(m, n, start_x, start_y):
    """
    Finds the route of a knight around a chessboard of dimensions m x n,
    starting from the initial position (start_x, start_y).
    Returns a 2D NumPy array representing the chessboard with move numbers,
    or None if the route does not exist.
    """
    # Initialize the visited array
    visited = np.zeros((m, n), dtype=int)

    # Possible moves for a knight
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    # Function to check if the knight has visited all cells
    def all_visited():
        return np.all(visited != 0)

    def knight_tour(x, y, move_count):
        visited[x][y] = move_count

        if move_count == m * n:
            return True

        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            if is_valid_move(next_x, next_y, m, n, visited):
                if knight_tour(next_x, next_y, move_count + 1):
                    return True

        visited[x][y] = 0

        return False

    # Start the knight tour from the initial position
    if knight_tour(start_x, start_y, 1) and all_visited():
        return visited

    return None

# Read input from file
with open('input.txt', 'r') as file:
    m, n = map(int, file.readline().split())
    start_x, start_y = map(int, file.readline().split())

# Find the knight route
with tqdm(total=m * n) as pbar:
    result = find_knight_route(m, n, start_x, start_y)
    pbar.update(m * n)

# Write output to file
with open('output.txt', 'w') as file:
    if result is None:
        file.write("Route does not exist")
    else:
        np.savetxt(file, result, fmt="%3d")
