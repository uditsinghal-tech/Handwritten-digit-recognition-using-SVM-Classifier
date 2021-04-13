#SVM classifier, training and prediction

import pandas as pd
import cv2
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

df=pd.read_csv("csv/dataset.csv")
print(df.shape)

X=df.drop(['label'],axis=1)
Y=df['label']
X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.25)

model=svm.SVC(gamma='auto',kernel='linear', C=2)
model.fit(X_train,Y_train)

print("Accuracy of the model is: ",model.score(X_test,Y_test))

img = cv2.imread("test_image/image.png", 0)
roi = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
rows,cols = roi.shape
X=[]
for i in range(rows):
	for j in range(cols):
		k = roi[i,j]
		if k>100:
			k=1
		else:
			k=0
		X.append(k)
predictions = model.predict([X])
print("Prediction: ", predictions[0])
cv2.putText(img, "Prediction is: "+str(predictions[0]), (20, 20), 0, 0.8, (255,0,0), 2, cv2.LINE_AA)
cv2.imshow("Prdediction", img)
cv2.waitKey(5000)