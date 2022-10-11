from PIL import ImageEnhance,Image
import glob

img = Image.open("/Users/adityabiswal/Desktop/computer_vision/peakpx (1).jpg")

#resizing the image
print(img.size)

#new size ratio for the image
newsize = (300,300)
img_resized = img.resize(newsize)
print(img_resized.size)
img_resized.save("resized.jpg")


#adjusting the brightness of the image
enhancer = ImageEnhance.Brightness(img)
img_light = enhancer.enhance(1.8)
img_light.save("brightened.jpg")


#converting image to grayscale image
img = img.convert('L')
img.save("grayscaled.jpg")




