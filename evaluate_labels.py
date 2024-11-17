import os


def count_bombs(grid, row, col, rows, cols):
    bomb_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
            bomb_count += 1
    return bomb_count


def process_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    # Create a new grid to store the result
    result = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                result[r][c] = -1
            elif grid[r][c] == 0:
                result[r][c] = count_bombs(grid, r, c, rows, cols)

    return result


def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def read_grid_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(map(int, line.split())))
    return grid


def write_grid_to_file(file_path, grid):
    with open(file_path, 'w') as file:
        for row in grid:
            file.write(" ".join(map(str, row)) + "\n")


def process_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        print(f"Processing file: {filename}")
        grid = read_grid_from_file(file_path)
        processed_grid = process_grid(grid)
        write_grid_to_file(file_path, processed_grid)
        print(f"Processed grid saved to {file_path}")

board_sizes = ["8x8", "16x16", "16x30"]
for board_size in board_sizes:
    directory_path = f"labels {board_size}"
    process_files_in_directory(directory_path)
