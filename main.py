from PIL import Image
import sys

def ImageToAscii(inFile):
	im = Image.open(inFile).convert('L')
	width = im.size[0]
	height = im.size[1]
	
	maxDimension = 100
	
	if (height > maxDimension or width > maxDimension):
		ratio = height/maxDimension
		if (width > height):
			ratio = width/maxDimension
		height /= ratio
		width /= ratio
		im = im.resize([width,height], Image.ANTIALIAS)
	
	imData = im.load()
	asciiList = ['@','8','O','o',':','.',' ',' ']
	out = []
	for x in range(height):
		line = ""
		for y in range(width):
			b = int(imData[y,x] / 36)
			line += asciiList[b]
		out[x] = line
	return out

def ImageToAsciiTextFile(inFile, outFile):
	out = ImageToAscii(inFile)
	f = open(outFile, 'w')
	for x in range(len(out)):
		f.write(out[x] + '\n')
	f.close()

if __name__ == "__main__":
	if len(sys.argv == 3):
		inFile = sys.argv[1]
		outFile = sys.argv[2]
		ImageToAsciiTextFile(inFile, outFile)
	else:
		#todo - throw in some error message here
