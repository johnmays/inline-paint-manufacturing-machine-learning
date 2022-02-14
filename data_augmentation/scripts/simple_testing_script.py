# the dimensions of the source images (5:4)
source_image_dimensions = (1280, 1024)
# 1024x1024 are the recommended largest dimensions
crop_dimensions = (256, 256)
for x in range(0, source_image_dimensions[0], crop_dimensions[0]):
    for y in range(0, source_image_dimensions[1], crop_dimensions[1]):
        print(str((x, y)), ", ", str(
            (x+crop_dimensions[0], y+crop_dimensions[1])))
