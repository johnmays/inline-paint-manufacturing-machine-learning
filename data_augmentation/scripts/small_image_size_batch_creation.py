from PIL import Image
import os
import matplotlib.pyplot as plt
new_image_dimensions = (256, 256)
number_of_images_from_source = 1
dispersion_times = ['01', '03', '08', '15']
print("Dimension of new images: " + str(new_image_dimensions[0]) + " x " + str(new_image_dimensions[1]))

source_data_location = '/Users/johnmays/Documents/Wirth Lab/still_data/dataset_1/'
augmented_data_location = '/Users/johnmays/Documents/Wirth Lab/still_data/small_datasets/'
os.chdir(source_data_location)

# Create Directories:

os.chdir(augmented_data_location)
new_dir_name = str(new_image_dimensions[0]) + "_" + str(new_image_dimensions[1])
os.makedirs(new_dir_name)
os.chdir(augmented_data_location + new_dir_name)
for dispersion_time in dispersion_times:
  os.makedirs(dispersion_time)


# Find smallest number of images in one source directory
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


