# First attempt to build an ANN


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
print(X)
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Import Keras library and modules
import keras
from keras.models import Sequential
from keras.layers import Dense

# Create the ANN
# It will be called 'classifier'
classifier = Sequential()

# Create the input layer and the first hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform',activation = 'relu', input_dim = 11))

# Creating a second layer
classifier.add(Dense(output_dim = 7, init = 'uniform',activation = 'relu'))

# Creating a second layer
classifier.add(Dense(output_dim = 4, init = 'uniform',activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform',activation = 'sigmoid'))

# Compiling the ANN
# Adam is a stochastic gradient method
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

# Fitting classifier to the Training set
classifier.fit(X_train,y_train,batch_size = 10,epochs = 30)



# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)