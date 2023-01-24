# !pip install anvil-uplink         (harus di uncomment jika dijalankan pada google colab)
import anvil.server
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from google.colab import drive      # Library hanya dapat dijalankan pada google colab
import matplotlib.pyplot as plt
# %matplotlib inline                (harus di uncomment jika dijalankan pada google colab)

plt.style.use('seaborn-poster')
anvil.server.connect("NGYRTN76HI6JORSCUQFVKJO7-7ESA5W76U4YVFPHB")

# Read data from CSV file
drive.mount('/content/drive')
path = '/content/drive/My Drive/Dataset/lungCancer.csv'
lungCancer_dataset = pd.read_csv(path)

# Replace dictionary
dict = {
  'YES':1,
  'NO':0,
  'M':1,
  'F':0,
  2:1,
  1:0
}

lungCancer_dataset_replaced = lungCancer_dataset.replace(dict)
lungCancer_dataset_replaced1 = lungCancer_dataset_replaced.drop(columns="AGE", axis=1)
lungCancer_dataset_replaced2 = lungCancer_dataset_replaced1.drop(columns="GENDER", axis=1)

# Split Attribute and Lable
x = lungCancer_dataset_replaced2[lungCancer_dataset_replaced2.columns[:13]]
y = lungCancer_dataset_replaced2['LUNG_CANCER']

# Normalization (Make the data scale consistent)
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

# Split data training and data testing
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Create SVC object and call fit function for training model 
clf = SVC(kernel='linear')
clf.fit(X_train,y_train)


# Web server

@anvil.server.callable
def cancer_predict(
  smoke,
  yellow_finger,
  anxious,
  friends,
  chronic_disease,
  fatigue,
  allergies,
  wheezing,
  alcohol,
  cough,
  breath,
  swallowing,
  chest_pain
):
  if(smoke == 'NO'): smoke = 0
  elif(smoke == 'YES'): smoke = 1
  
  if(yellow_finger == 'NO'): yellow_finger = 0
  elif(yellow_finger == 'YES'): yellow_finger = 1
  
  if(anxious == 'NO'): anxious = 0
  elif(anxious == 'YES'): anxious = 1
  
  if(friends == 'NO'): friends = 0
  elif(friends == 'YES'): friends = 1
  
  if(chronic_disease == 'NO'): chronic_disease = 0
  elif(chronic_disease == 'YES'): chronic_disease = 1
  
  if(fatigue == 'NO'): fatigue = 0
  elif(fatigue == 'YES'): fatigue = 1
  
  if(allergies == 'NO'): allergies = 0
  elif(allergies == 'YES'): allergies = 1
  
  if(wheezing == 'NO'): wheezing = 0
  elif(wheezing == 'YES'): wheezing = 1
  
  if(alcohol == 'NO'): alcohol = 0
  elif(alcohol == 'YES'): alcohol = 1
  
  if(cough == 'NO'): cough = 0
  elif(cough == 'YES'): cough = 1
  
  if(breath == 'NO'): breath = 0
  elif(breath == 'YES'): breath = 1
  
  if(swallowing == 'NO'): swallowing = 0
  elif(swallowing == 'YES'): swallowing = 1
  
  if(chest_pain == 'NO'): chest_pain = 0
  elif(chest_pain == 'YES'): chest_pain = 1
  
  input = [
    smoke,
    yellow_finger,
    anxious,
    friends,
    chronic_disease,
    fatigue,
    allergies,
    wheezing,
    alcohol,
    cough,
    breath,
    swallowing,
    chest_pain
  ]
  
  input_as_array = np.asarray(input)
  input_reshape = input_as_array.reshape(1,-1)

  std_data = scaler.transform(input_reshape)
  prediction = clf.predict(std_data)

  if (prediction == 1):
    return 'This patient possibly positive lung cancer'
  elif (prediction == 0):
    return 'This patient possibly negative lung cancer'
  else:
    return 'Wrong input!'
  

# Runserver anvil
anvil.server.wait_forever()