# Necessary Imports:

from PIL import Image
import os
import matplotlib.pyplot as plt
import math

"""Note: the purpose of this script is to parse the source data directories, full of .TIFs, and for each .TIF, \
chop it up into equally sized subimages, then take each subimage and produce 4 separate rotated images, and finally put all  \
of them into the approprate new directory. 
"""

# the dimensions of the source images (5:4)
source_image_dimensions = (1280, 1024)
# 1024x1024 are the recommended largest dimensions
crop_dimensions = (256, 256)
pool = False  # set to true if you want pooling to take place
pool_dimensions = (256, 256)  # 32x32 are the recommended smallest dimensions
number_of_images_from_source = 20
dispersion_times = ['01', '03', '08', '15']
print("Dimension of new images: " +
      str(crop_dimensions[0]) + " x " + str(crop_dimensions[1]))

source_data_location = '/Users/johnmays/Documents/Wirth Lab/still_data/dataset_1/'
augmented_data_location = '/Users/johnmays/Documents/Wirth Lab/still_data/small_datasets/'
os.chdir(source_data_location)

# Create Directories:

os.chdir(augmented_data_location)
new_dir_name = str(
    "Post-Hinc" + crop_dimensions[0]) + "_" + str(crop_dimensions[1])
if pool:
    new_dir_name = new_dir_name + "pooled_to" + \
        str(pool_dimensions[0]) + "_" + str(pool_dimensions[1])
os.makedirs(new_dir_name)
os.chdir(augmented_data_location + new_dir_name)
for dispersion_time in dispersion_times:
    os.makedirs(dispersion_time)


# Find smallest number of images in a source directory; which will be the limiting number, in order to evenly represent the dispersion times
min_number_of_images_in_subdirectory = 1000000

os.chdir(source_data_location)
for subdirectory in os.listdir(source_data_location):
    if(subdirectory != '.DS_Store'):
        number_of_images_in_subdirectory = 0
        for filename in os.listdir(source_data_location + subdirectory):
            if filename.endswith('.tif'):
                number_of_images_in_subdirectory += 1
        if number_of_images_in_subdirectory < min_number_of_images_in_subdirectory:
            min_number_of_images_in_subdirectory = number_of_images_in_subdirectory

# generating crop coordinates:
crop_coordinates = []
top_corner = (0, 0)
bottom_corner = crop_dimensions

for x in range(0, source_image_dimensions[0], crop_dimensions[0]):
    for y in range(0, source_image_dimensions[1], crop_dimensions[1]):
        corner_coordinates = (
            x, y) + (x+crop_dimensions[0], y+crop_dimensions[1])
        crop_coordinates.append[corner_coordinates]


for dispersion_time in dispersion_times:
    destination_dir = augmented_data_location + new_dir_name + "/" + dispersion_time
    i = 0
    for filename in os.listdir(source_data_location + dispersion_time):
        i += 1
        if i > min_number_of_images_in_subdirectory:
            break
        elif filename.endswith('.tif'):
            os.chdir(source_data_location + dispersion_time)
            img = Image.open(filename)
            os.chdir(destination_dir)
            # L, T, R, B (does not include pixel on bottom-right coordinate)
            cropped_img = img.crop(crop_coordinates)
            if not pool:
                cropped_img.save(
                    filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_0' + '.tif')
                cropped_img.rotate(90).save(
                    filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_90' + '.tif')
                cropped_img.rotate(180).save(
                    filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_180' + '.tif')
                cropped_img.rotate(270).save(
                    filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_270' + '.tif')
            else:
                resized_img = cropped_img.resize(pool_dimensions)
                resized_img.save(
                    filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_0' + '.tif')
                resized_img.rotate(90).save(
                    filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_90' + '.tif')
                resized_img.rotate(180).save(
                    filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_180' + '.tif')
                resized_img.rotate(270).save(
                    filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_270' + '.tif')
        else:
            continue
