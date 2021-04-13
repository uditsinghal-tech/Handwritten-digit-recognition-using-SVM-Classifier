#This code is used to create the csv file from input dataset of images
import cv2
import numpy as np
import csv
import glob
f = open('csv/dataset.csv', 'a')
writer = csv.writer(f)
header = ["label"]
for i in range(784):
	header.append("pixel_" + str(i))
writer.writerow(header)

labels = ["0","1","2","3","4","5","6","7","8","9"]

for label in labels:
	dirList = glob.glob("Images/"+label+"/*.png")
	for img_path in dirList:
		im_gray = cv2.imread(img_path,0)
		roi = cv2.resize(im_gray, (28, 28), interpolation=cv2.INTER_AREA)
		data=[]
		data.append(label)
		rows,cols = roi.shape
		for i in range(rows):
			for j in range(cols):
				k = roi[i,j]
				if k>100:
					k=1
				else:
					k=0
				data.append(k)
		writer.writerow(data)
