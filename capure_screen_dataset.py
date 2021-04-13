#This code can be used to generate a dataset manually
import pyscreenshot as ImageGrab
import time
#Images of all digits 0,1,2,3,4,5,6,7,8,9 can be created one by one
images_folder = "Images/0/"

for i in range (0,90):
	time.sleep(7)
	im = ImageGrab.grab(bbox=(80, 80, 208, 208)) # X1,Y1,X2,Y2
	print ("saved...",i)
	im.save(images_folder+str(i)+'.png')
	print ("Clear the screen now and redraw...")
	