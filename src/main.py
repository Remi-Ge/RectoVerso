import os
from PIL import Image
from image_processor.decoder import ImageDecoder

#example file x: 8, y: 12
file_path = input('File path: ')

dimension_x, dimension_y = input('Dimension X: '), input('Dimension Y: ')

image_decoder = ImageDecoder(file_path, 8, 12)


size = image_decoder.image_tiles[0].size
new_image = Image.new("RGB", (size[0] * len(image_decoder.order[0]), size[1] * len(image_decoder.order[1])), (255, 255, 255))
for y in range(len(image_decoder.order)):
    for x in range(len(image_decoder.order[0])):
        if image_decoder.order[y][x] == -1:
            continue
        new_image.paste(image_decoder.image_tiles[image_decoder.order[y][x]], (x * size[0], y * size[1]))

base, ext = os.path.splitext(file_path)
new_file_path = base + "_corrected" + ext
new_image.save(new_file_path)
