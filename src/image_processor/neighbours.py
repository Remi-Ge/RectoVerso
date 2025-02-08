from PIL import Image

def compare_colors(color1, color2):
    # Remove alpha channel
    color1 = color1[:3]
    color2 = color2[:3]
    difference = (abs(color1[0] - color2[0]) + abs(color1[1] - color2[1]) + abs(color1[2] - color2[2])) / 3
    return difference

def get_neighbours(tiles):
    estimated_neighbours = {}
    for i in range(len(tiles)):
        estimated_neighbours[i] = compare_tile(tiles, i)
        print(f'Recherche: {round(i / len(tiles) * 100, 1)} %')
    corrected_neighbours = {}
    for i in estimated_neighbours:
        corrected_neighbours[i] = {key: None for key in ['left', 'top', 'right', 'bottom']}

        if navigate(estimated_neighbours, i, ['left', 'top']) == navigate(estimated_neighbours, i, ['top', 'left']) != i:
            corrected_neighbours[i]['left'] = estimated_neighbours[i]['left'][0]
            corrected_neighbours[i]['top'] = estimated_neighbours[i]['top'][0]

        if navigate(estimated_neighbours, i, ['top', 'right']) == navigate(estimated_neighbours, i, ['right', 'top']) != i:
            corrected_neighbours[i]['top'] = estimated_neighbours[i]['top'][0]
            corrected_neighbours[i]['right'] = estimated_neighbours[i]['right'][0]
        
        if navigate(estimated_neighbours, i, ['right', 'bottom']) == navigate(estimated_neighbours, i, ['bottom', 'right']) != i:
            corrected_neighbours[i]['right'] = estimated_neighbours[i]['right'][0]
            corrected_neighbours[i]['bottom'] = estimated_neighbours[i]['bottom'][0]
        
        if navigate(estimated_neighbours, i, ['bottom', 'left']) == navigate(estimated_neighbours, i, ['left', 'bottom']) != i:
            corrected_neighbours[i]['bottom'] = estimated_neighbours[i]['bottom'][0]
            corrected_neighbours[i]['left'] = estimated_neighbours[i]['left'][0]
    return corrected_neighbours

def compare_tile(tiles, tile_index):
    tile_size_x, tile_size_y = tiles[0].size
    min_differences = {key: [-1, None] for key in ['left', 'top', 'right', 'bottom']}
    for i in range(len(tiles)):
        if i == tile_index:
            continue
        differences = {key: 0 for key in ['left', 'top', 'right', 'bottom']}
        for x in range(tile_size_x):
            differences['top'] += compare_colors(tiles[tile_index].getpixel((x, 0)),
                                    tiles[i].getpixel((x, tile_size_y - 1))) / tile_size_x
            differences['bottom'] += compare_colors(tiles[tile_index].getpixel((x, tile_size_y - 1)),
                                    tiles[i].getpixel((x, 0))) / tile_size_x
        for y in range(tile_size_y):
            differences['left'] += compare_colors(tiles[tile_index].getpixel((0, y)),
                                    tiles[i].getpixel((tile_size_x - 1, y))) / tile_size_y
            differences['right'] += compare_colors(tiles[tile_index].getpixel((tile_size_x - 1, y)),
                                    tiles[i].getpixel((0, y))) / tile_size_y
        for key in differences:
            if not min_differences[key][1] or differences[key] < min_differences[key][1]:
                min_differences[key][0] = i
                min_differences[key][1] = round(differences[key], 3)
    return min_differences

def navigate(neighbours, start, directions):
    # start: id
    # direction: list of directions, ['left', 'right']
    position = start
    for d in directions:
        position = neighbours[position][d][0]
    return position