from PIL import Image
import os
import matplotlib.pyplot as plt
crop_dimensions = (1024, 1024)  # 1024x1024 are the recommended largest dimensions
pool = False  # set to true if you want pooling to take place
pool_dimensions = (32, 32)  # 32x32 are the recommended smallest dimensions
number_of_images_from_source = 1
dispersion_times = ['01', '03', '08', '15']
print("Dimension of new images: " + str(crop_dimensions[0]) + " x " + str(crop_dimensions[1]))

source_data_location = '/Users/johnmays/Documents/Wirth Lab/still_data/dataset_1/'
augmented_data_location = '/Users/johnmays/Documents/Wirth Lab/still_data/small_datasets/'
os.chdir(source_data_location)

# Create Directories:

os.chdir(augmented_data_location)
new_dir_name = str(crop_dimensions[0]) + "_" + str(crop_dimensions[1])
if pool:
    new_dir_name = str(pool_dimensions[0]) + "_" + str(pool_dimensions[1]) + "_pooled_from_" + str(crop_dimensions[1])
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

# generating crop coordinates:
crop_coordinates = (int(640-crop_dimensions[0]/2), int(512-crop_dimensions[1]/2), int(640+crop_dimensions[0]/2), int(512+crop_dimensions[1]/2))
print(crop_coordinates)

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
            cropped_img = img.crop(crop_coordinates)  # L, T, R, B (does not include pixel on bottom-right coordinate)
            if not pool:
                cropped_img.save(filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_0' + '.tif')
                cropped_img.rotate(90).save(filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_90' + '.tif')
                cropped_img.rotate(180).save(filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_180' + '.tif')
                cropped_img.rotate(270).save(filename[0:-4] + '_' + str(crop_dimensions[0]) + '_cropped_270' + '.tif')
            else:
                resized_img = cropped_img.resize(pool_dimensions)
                resized_img.save(filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_0' + '.tif')
                resized_img.rotate(90).save(filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_90' + '.tif')
                resized_img.rotate(180).save(filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_180' + '.tif')
                resized_img.rotate(270).save(filename[0:-4] + '_' + str(pool_dimensions[0]) + '_cropped_pooled_270' + '.tif')
        else:
            continue


