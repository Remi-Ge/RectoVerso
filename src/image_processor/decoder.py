from PIL import Image
from .splitter import split_image
from .neighbours import get_neighbours
from .merge import merge_tiles

class ImageDecoder:
    def __init__(self, im_path, dimension_x, dimension_y):
        self.image = Image.open(im_path)
        self.image_tiles = split_image(self.image, dimension_x, dimension_y)
        neighbours = get_neighbours(self.image_tiles)
        self.order = merge_tiles(self.image_tiles, neighbours, dimension_x, dimension_y)
