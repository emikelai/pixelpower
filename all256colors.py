from PIL import Image


def main():
	im = Image.new('L', (16,16))	#create new 16x16pixel image
	print("Image size: ")
	print (im.size)	#print dimensions of image onto screen
	im.save('16x16.png','png')	#save 16x16 

	im16x16 = Image.open("16x16.png")	#open 16x16 pixel image
	pix = im16x16.load()	#load image for manipulation
	i=0
	j=0
	for i in range(0,16):	#for loop to insert one of each color per pixel for a 16x16 box with 
							#256 unique pixel colors
		for j in range(0,16):
			#print("16*1+j: %d" % (16*i+j))
			pix[j,i] = 16*i+j
			#print("pixel value: %d" % (16*i+j))

	im16x16.save('all256colors16x16img.png','png')

	#no need to convert to grayscale with two lines below because image created is of type 'L'
	#convertedBWimage = Image.open("all256colors16x16img.png").convert("L")
	#convertedBWimage.save('all256colors16x16imgBW.png','png')

if __name__ == "__main__":
	main()

