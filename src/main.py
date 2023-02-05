import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier,_tree
# this package is used to change raw feature vectors into a representation that is more suitable for some uses.
from sklearn import preprocessing as preprocess
# used to split the dataset into training and testing arrays
from sklearn.model_selection import train_test_split as tts
from sklearn.svm import SVC



# training and testing the data read from the csv files
train = pd.read_csv('../data/data.csv') 
test = pd.read_csv('../data/data.csv') # TODO update with test file when it's done
columns = train.columns
columns = columns[:-1]
x = train[columns]
y = train['label']

# transforming non-numerical labels to numerical labels
label_encoder = preprocess.LabelEncoder()
label_encoder.fit(y)
y = label_encoder.transform(y)

# splitting 33 percent of the data for testing and the rest is used for training
xTrain, xTest, yTrain, yTest = tts(x, y, test_size = 0.33)
testingX = test[columns]
testingY = test['label']
# transform into numerical labels
testingY = label_encoder.transform(testingY)


model1 =SVC()
model1.fit(xTrain,yTrain)
print("svm model: ")
print(model1.score(xTest,yTest))