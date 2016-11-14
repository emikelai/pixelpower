#this program generates random images width x height pixel images
#the color of each pixel is random, and the choice of colors from which to populate the pixels can
#come from a 1 (black and white), 8 (grayscale), or 24 bit (true color) color chart


from PIL import Image
from random import randint
from collections import Counter
import random


def rgb_int2tuple(rgbint):
    #return (rgbint // 256 // 256 % 256, rgbint // 256 % 256, rgbint % 256)
    rgb_tuple = (rgbint // 256 // 256 % 256, rgbint // 256 % 256, rgbint % 256)
    #print ("rgb_tuple from rgb_int2tuple function: {}".format(rgb_tuple))
    return rgb_tuple
    #http://stackoverflow.com/questions/2262100/rgb-int-to-rgb-python

def return_num_pixel_values(num, image):
	#input num (number of pixel colors to be returned)
	#input image (image is parsed in this function )
	#this function will return num pixel colors on which to build the image(s)
	#it takes the input image and goes through each pixel one by one and determines the highest occuring values
	#the intent is to build the width x height image using only the highest occuring colors of the input image

	src_img = Image.open(image) #open passed in image
	print("\nsrc image format, size, and mode: {} {} {}".format(src_img.format, (src_img.size,), src_img.mode)) #print for information
	#print("src image format, size, and mode: %s %s %s" % ((src_img.format, (src_img.size,), src_img.mode))) #print for information
	#above two lines optional ways to print

	#print(src_img.format, src_img.size, src_img.mode) #print for information
	#assign to variables to use in this definition
	(src_width,src_height) = src_img.size
	#print ("src_width,src_height: %d,%d" % (src_width,src_height))

	complete_list_of_colors_used = []
	#retrieve b/w or rgb values of each pixel in the input image
	for i in range(0,src_width):
		for j in range(0,src_height):
			pixelvalue = src_img.getpixel((i,j))	#get RGB value of each pixel, need if/elif depending on whether image is b/w or rgb
			#print("pixelvalue: {}".format(pixelvalue))
			if (src_img.mode == '1' or src_img.mode == 'L' or src_img.mode == 'P'):
				#append value to list of all pixels in black/white or grayscale
				complete_list_of_colors_used.append(pixelvalue)
				#print(pixelvalue)
				#return pixelvalue
			elif (src_img.mode == 'RGB'):
				(r,g,b) = pixelvalue
				#print(r,g,b)
				#append value to list of all pixels in rgb converted to integer
				complete_list_of_colors_used.append((r<<16) + (g<<8) + b) 	#translate rgb value to integer, apped to list
				#return pixelvalue
			else:
				print("In return_num_pixel_values() function, image is not a valid image mode of 1,L, or RGB")
	#print(complete_list_of_colors_used)
	most_commonX = Counter(complete_list_of_colors_used) #use standard library Counter class
	print(most_commonX.most_common(num))	#print most common occuring 'num' items
	return(most_commonX.most_common(num))

def color_mode(bpp_value):
	#input bpp_value is the bits per pixel desired output image(s)
	#this function returns a string whose value is the mode of the image being created
	#http://pillow.readthedocs.io/en/3.4.x/handbook/concepts.html#concept-modes
	if (bpp_value == 1):
		return '1'
	elif (bpp_value == 8):
		return 'L'
	elif (bpp_value == 24):
		return 'RGB'
	else:
		print("In color_mode() function, please provide valid bpp_value: 1,8,256")

def main():

	width = 300 #width of generated image in pixels
	height = 300 #height of generated image in pixels
	bpp = 24	#bits per pixel, choose either 1 for B/W, 8 for grayscale, 24 for truecolor

	#bpp_str = str(bpp) #convert integer to string for use in Image.new
	#im = Image.new(bpp_str, (width,height))	#create new width x heightpixel image
	im = Image.new(color_mode(bpp), (width,height))	#create new width x heightpixel image
	print("Image size: ")
	print (im.size)	#print dimensions of image onto screen
	im.save('%sx%s.png' % (width, height),'png')	#save width x height 

	im = Image.open("%sx%s.png" % (width,height))	#open width x height pixel image
	pix = im.load()	#load image for manipulation
	i=0
	j=0
	max_rand_number = 2**bpp	#define upper end of range that each pixel can have
	print ("max_rand_number: %d" % max_rand_number)
	
	src_pixel_and_cnt_list = return_num_pixel_values(100,'homer.jpg') #will return a list of tuples containing most common pixel colors in source image
																			   #and the number of occurences of that pixel list
	src_pixel_list = [i[0] for i in src_pixel_and_cnt_list]	#obtain just the pixel values and create list
	#print(src_pixel_list)
	for i in range(0,height):	#for loop to insert one of each color per pixel for a width x height box with 
							#256 unique pixel colors
		for j in range(0,width):
			pix[j,i] = rgb_int2tuple(random.choice(src_pixel_list))#randint(0,max_rand_number)#(0,36,244)#randint(0, max_rand_number) #populate each pixel in the picture
			#print("pixel value printed in main(): {}".format(pix[j,i]))

	im.save('all2colors%sx%simg.png' % (width, height),'png')
	print("Generated image: all2colors%sx%simg.png" % (width, height))

	#no need to convert to grayscale with two lines below because image created is of type 'L'
	#convertedBWimage = Image.open("all256colorswidth x heightimg.png").convert("L")
	#convertedBWimage.save('all256colorswidth x heightimgBW.png','png')

if __name__ == "__main__":
	main()

