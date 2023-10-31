import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv('train_dataset1.csv')

le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])
input_cols = ['Gender',
               'Age',
               'do you enjoy thinking about abstract concept and theories',
               'would you say that you have a vivid imagination',
               'are you open to different cultures and way of life',
               'do you enjoy trying new foods and cuisines',	
               'would you say that you are creative',	
               'would you say that you are organized and responsible',	
               'do you value punctuality and meeting deadlines',	
               'are you a planner and do you like to set goals for yourself',	
               'would you say that you are reliable and dependable',	
               'do you pay attention to details and try to avoid mistakes',	
               'do you enjoy being around people and socialization',
                'do you feel energized and recharged after spending time with others',	
                'would you say that you are outgoing and talkative',	
                'do you enjoy being the center of attention',	
                'do you enjoy participation in group activity',	
                'would you say that you are friendly and compassionate',	
                'do you value cooperation and harmony in your relationships',	
                'are you sensitive to other peoples feelings',	
                'would you say that you are a good listener',
                'do you avoid conflict and try to find compromise solution',	
                'do you tend to worry a lot and feel anxious',	
                'are you easily upset or frustrated by small things',	
                'would you say that you are emotionally unstable',	
                'do you have a tendency to be self-critical and negative',	
                'do you feel overwhelmed by stress',
                'Are you interested in trying new things and exploring different ideas',
                'Do you enjoy traveling to new places',
                'Do you enjoy reading and learning about different topics',
                'Would you say that you have a philosophical side',
                'Do you enjoy taking risks and trying things outside of your comfort zone',
                'Do you feel guilty if you dont fulfill your responsibilities',
                'Would you say that you are disciplined and self-controlled',
                'Do you tend to follow rules and regulations',
                'Would you say that you are hardworking and dedicated',
                'Do you value order and structure in your life',
                'Would you say that you are assertive and confident',
                'Do you enjoy meeting new people and making new friends',
                'Do you prefer to work in a team rather than alone',
                'Would you say that you have a wide circle of friends',
                'Do you enjoy parties and other social events',
                'Would you say that you are patient and understanding',
                'Do you value kindness and generosity',
                'Do you feel empathy towards others',
                'Do you tend to forgive easily',
                'Do you believe in treating others the way you would like to be treated',
                'Do you have a tendency to be moody and unpredictable',
                'Do you feel easily hurt or offended by others',
                'Do you have a tendency to dwell on negative experiences',
                'Would you say that you are sensitive and easily moved to tears',
                'Do you have a tendency to catastrophize and imagine worst-case scenarios']

output_cols = ['Personality (Class label)']

scaler = StandardScaler()
data[input_cols] = scaler.fit_transform(data[input_cols])
data.head()

X = data[input_cols]
Y = data[output_cols]

model = LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
model.fit(X, Y)  

test_data = pd.read_csv('test_dataset1.csv')
test_data['Gender'] = le.fit_transform(test_data['Gender'])
test_data[input_cols] = scaler.fit_transform(test_data[input_cols])
X_test = test_data[input_cols]
# Y_test = test_data['Personality (class label)']
Y_test = test_data['Personality (class label)'].values.ravel()

test_data.head()

y_pred= model.predict(X_test)  

print(accuracy_score(Y_test,y_pred)*100)

joblib.dump(model, "train_model1.pkl")