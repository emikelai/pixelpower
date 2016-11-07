from PIL import Image
from random import randint

def color_mode(bpp_value):
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

	width = 3 #width of generated image in pixels
	height = 3 #height of generated image in pixels
	bpp = 1	#bits per pixel, choose either 1 for B/W, 8 for grayscale, 24 for truecolor

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
	max_rand_number = 2**bpp
	print ("max_rand_number: %d" % max_rand_number)
	for i in range(0,height):	#for loop to insert one of each color per pixel for a width x height box with 
							#256 unique pixel colors
		for j in range(0,width):
			#print("16*1+j: %d" % (16*i+j))
			pix[j,i] = randint(0, max_rand_number)
			#print("pixel value: %d" % (16*i+j))

	im.save('all2colors%sx%simg.png' % (width, height),'png')
	print("Generated image: all2colors%sx%simg.png" % (width, height))
	# generated_image = Image.open('all2colorswidth x heightimg.png')
	# im = generated_image.load()
	# im.show()

	#no need to convert to grayscale with two lines below because image created is of type 'L'
	#convertedBWimage = Image.open("all256colorswidth x heightimg.png").convert("L")
	#convertedBWimage.save('all256colorswidth x heightimgBW.png','png')

if __name__ == "__main__":
	main()

