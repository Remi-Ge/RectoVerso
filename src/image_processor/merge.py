from PIL import Image

def merge_tiles(tiles, neighbours, dimension_x, dimension_y):
    grid = [[-1 for k in range(dimension_x * 2)] for k in range(dimension_y * 2)]
    def add_to_grid(x, y, index):
        if index == None:
            return
        if x >= len(grid[0]) or y >= len(grid) or x < 0 or y < 0:
            return
        if grid[y][x] == index:
            return
        if grid[y][x] != -1:
            return
        grid[y][x] = index
        add_to_grid(x-1, y, neighbours[index]['left'])
        add_to_grid(x, y-1, neighbours[index]['top'])
        add_to_grid(x+1, y, neighbours[index]['right'])
        add_to_grid(x, y+1, neighbours[index]['bottom'])
    add_to_grid(dimension_x, dimension_y, 0)
    return grid
