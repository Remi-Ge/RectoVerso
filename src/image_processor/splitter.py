from PIL import Image

def split_image(image: Image, dimension_x, dimension_y):
    taille_size_x, taille_size_y = image.size[0] / dimension_x, image.size[1] / dimension_y
    if round(taille_size_x) != taille_size_x or round(taille_size_y) != taille_size_y:
        raise Exception('Image size not divisible by the grid dimension')
    image_slices = []
    for y in range(dimension_y):
        for x in range(dimension_x):
            slice = image.crop((x * taille_size_x, y * taille_size_y,
                                x * taille_size_x + taille_size_x,
                                y * taille_size_y + taille_size_y))
            image_slices.append(slice)
    return image_slices