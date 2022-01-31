import numpy as np
from PIL import Image
import os
# from queue import Queue
# from threading import Thread
# from time import time

# Two thresholds are defined (black and white) and pixels are changed
# To either 100% white or relativly close to black

def filter_threshold(img_array):
	"""
	Her defineres funktionen som fjerner salt og peber støj
	input: 2D np array af billedet
	returnerer: ny np.array af billedet med mindre "støj"
	"""
	size = img_array.shape
	for x in range(size[0]):
		for y in range(size[1]):
			if img_array[x, y] <= 50:
				img_array[x, y] = 0

			elif img_array[x, y] >= 150:
				img_array[x, y] = 255
	print("Threshold filtering done")			
	return img_array


def closest_multiple(num_lines, p):
	if(num_lines % p):# := if(0) == if(False)
		return x-(x%p) #num_lines?
	else:
		return num_lines


def filter_threshold_pll(img_array, num_cores):
	for x in range(size[0]):
		for y in range(size[1]):
			if img_array[x, y] <= 50:
				img_array[x, y] = 0

			elif img_array[x, y] >= 150:
				img_array[x, y] = 255

	print("Threshold filtering done")			
	return img_array


def remove_isolated_pixels(img_array):
	size = img_array.shape
	"""
	loop where we define how fine we want the filtering
	"""
	pixels_turned_on = 0

	for i in range(size[0]-3):
		for j in range(size[1]-3): #3 er arbitrær, så vi ikke overskrider
			if img_array[i,j] != 255:
				pixels_turned_on +=1

				#Looking 2 pixels up on y-axis
				for pixels in range(2):
					if img_array[i-pixels,j] != 255:
						pixels_turned_on +=1

				#Looking 3 pixels down on y-axis	
				for pixels in range(2):
					if img_array[i+pixels,j] != 255:
						pixels_turned_on +=1

				#Looking 3 pixels right on x-axis			
				for pixels in range(2):
					if img_array[i,j+pixels] !=255:
						pixels_turned_on +=1
				if pixels_turned_on <= 4:
					img_array[i,j] = 255		
			pixels_turned_on = 0
	print("Single pixels removed")		
	return img_array 				


def remove_2x1_pixels(img_array):
	size = img_array.shape

	"""
	Where we remove 2x1 pixel objects
	"""
	white_pixels = 0

	for i in range(size[0]-2):
		for j in range(size[1]-2): #2 er arbitrær, så vi ikke overskrider
			if img_array[i,j] != 255:

				#Looking if pixel above is at value 255
				if img_array[i-1,j] == 255:
					white_pixels += 1

				#Looking if pixel to the right is at value 255
				if img_array[i,j+1] == 255:
					white_pixels += 1

				#Looking if the 2nd pixel below is at value 255
				if img_array[i+2,j] == 255:
					white_pixels += 1

				#Looking if pixel the the left is at value 255
				if img_array[i,j-1] == 255:
					white_pixels += 1

				if white_pixels == 4:
					img_array[i,j] = 255
					img_array[i+1,j] = 255

			white_pixels = 0
	print("2x1 blobs removed")		
	return img_array 			

###############################################
#    Functions defined: ok || main loop:      #
###############################################

img = Image.open("test_pic.tiff").convert("L")
img_array = np.array(img)

print(img_array.shape)

img_array_th_fltrd = filter_threshold(img_array)

for _ in range(2):

	img_array_final = remove_isolated_pixels(img_array_th_fltrd)

two_by_one_pixels = remove_2x1_pixels(img_array_final)

print("Done!")

im = Image.fromarray(img_array)
im.save("ouputs/denoised.tiff")
