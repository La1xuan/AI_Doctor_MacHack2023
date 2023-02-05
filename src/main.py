import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier,_tree
# this package is used to change raw feature vectors into a representation that is more suitable for some uses.
from sklearn import preprocessing as preprocess
# used to split the dataset into training and testing arrays
from sklearn.model_selection import train_test_split as tts
from sklearn.model_selection import cross_val_score as cvs
from sklearn.svm import SVC
import warnings
import copy
warnings.filterwarnings("ignore", category=UserWarning)

symptoms = ['arm pain', 'back pain', 'leg pain', 'ankle pain', 'inner thigh pain', 'back thigh pain', 'shoulder pain', 'tendon pain', 'swelling','headache', 'weakness', 'stiffness', 'difficulty moving/straightening ','nausea', 'bruising ', 'tenderness', 'numbness','difficulty putting weight on', 'dizziness or blurry vision', 'spasms','elbow pain', 'difficulty balancing ', 'light and sound irritation',' Trouble controlling bowels or bladder']

treatment = {"sprained ankle": """sprained ankle\n Suggested Treatment:\n Rest, Ice, Compression, and Elevation (or) ankle support brace"""
            , "Knee injury (ACL tear, MCL tear)": """Knee injury (ACL tear, MCL tear)\n Suggested Treatment:\n ACL or MCL reconstruction (or) rehabilitation with orthopedic therapy"""
            , "shin splints": """shin splints\n Suggested Treatment:\n Nonsteroidal anti-inflammatory medicines"""
            , "tennis elbow (lateral epicondylitis)": """tennis elbow (lateral epicondylitis)\n Suggested Treatment:\n Counterforce brace. Steroid injections"""
            , "groin pull (groin strain)": """groin pull (groin strain)\n Suggested Treatment:\n Ice pack"""
            , "hamstring strain": """hamstring strain\n Suggested Treatment:\n Physical therapy"""
            , "shoulder impingement": """shoulder impingement\n Suggested Treatment:\n Shoulder exercises"""
            , "low back pain": """low back pain\n Suggested Treatment:\n Acupuncture"""
            , "herniated disc in the neck": """herniated disc in the neck\n Suggested Treatment:\n Anterior cervical discectomy & fusion (ACDF)"""
            , "tendonitis": """tendonitis\n Suggested Treatment:\n rest, physical therapy and medicine"""
            , "concussion ": """concussion\n Suggested Treatment:\n Physical and mental rest"""
            , "Sciatica": """Sciatica\n Suggested Treatment:\n Anti-inflammatories. Corticosteroids. Antidepressants. Anti-seizure medications. Opioids"""
            }
def diagnose(record):
    # training and testing the data read from the csv files
    train = pd.read_csv('./data/test1.csv') 
    test = pd.read_csv('./data/test1.csv') # TODO update with test file when it's done
    #reading = pd.read_csv('../data/test.csv')
    columns = train.columns
    columns = columns[:-1]
    x = train[columns]
    y = train['injury']

    # transforming non-numerical labels to numerical labels
    label_encoder = preprocess.LabelEncoder()
    label_encoder.fit(y)
    z = y
    y = label_encoder.transform(y)

    # splitting 33 percent of the data for testing and the rest is used for training
    xTrain, xTest, yTrain, yTest = tts(x, y, test_size = 0.33)
    testingX = test[columns]
    testingY = test['injury']
    # transform into numerical labels
    testingY = label_encoder.transform(testingY)


    classification  = DecisionTreeClassifier()
    classification1 = classification.fit(xTrain,yTrain)
    scores = cvs(classification1, xTest, yTest, cv=3)
    print(classification1.predict(xTest))

    print ("Mean", scores.mean())

    model1 = SVC()
    model1.fit(xTrain,yTrain)
    print("svm model: ")
    print(model1.score(xTest,yTest))

    featureImp = classification1.feature_importances_
    indices = np.argsort(featureImp)[::-1]
    attributes = columns
    #print(classification1.predict(xTest))
    z = (classification1.predict(pd.DataFrame([record], columns =xTest.columns)))
    z = label_encoder.inverse_transform(z)
    print(treatment[z[0]])
    return treatment[z[0]]
#print(reading)
#print(xTest)
#print(model1.predict(xTest))
#print(yTest)