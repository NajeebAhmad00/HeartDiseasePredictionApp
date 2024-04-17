import numpy as np
import joblib

model = joblib.load('heart_disease_model.pkl')

print('NOTE: THIS APPLICATION HAS A SLIGHT BUG!')

age = int(input('Enter age: '))
sex = input('\nIs the patient male of female? (M/F): ')
cp = int(input('\nSelect chest pain type:\n 0. Typical Angina\n 1. Atypical Angina\n 2. Non-Anginal\n 3. Asymptotic\nEnter the corresponding number from above: '))
trestbps = int(input('\nEnter resting blood pressure (in mm Hg): '))
chol = int(input('\nEnter cholesterol level: '))
fbs = input('\nIs the blood sugar greater than 120 mg/dl while fasting? (Yes/No): ')
restecg = int(input('\nSelect resting ECG results:\n 0. Normal\n 1. stt abnormality\n 2. lv hypertrophy\nSelect the corresponding number from above: '))
thalach = int(input('\nEnter max heart rate achieved: '))
exang = input('\nIs there exercise-induced angina (Yes/No): ')
oldpeak = float(input('\nValue of ST depression induced by exercise relative to rest: '))
slope = int(input('\nSelect the slope of the peak exercise ST segment:\n 0. Upsloping\n 1. Flat\n 2. Downsloping\nEnter the corresponding number from above: '))
ca = int(input('\nEnter number of major vessels (ranges from 0-3): '))
thal = int(input('\nSelect that applies:\n 0. Normal\n 1. Fixed defect\n 2. Reversible defect\nEnter your response: '))

if sex == 'M':
    converted_sex = 0
else:
    converted_sex = 1

if fbs == 'Yes':
    converted_fbs = 1
else:
    converted_fbs = 0

if exang == 'Yes':
    converted_exang = 1
else:
    converted_exang = 0

data = np.array((
    age,
    converted_sex,
    cp,
    trestbps,
    chol,
    converted_fbs,
    restecg,
    thalach,
    converted_exang,
    oldpeak,
    slope,
    ca,
    thal
)).reshape(1, -1)

prediction = model.predict(data)

if prediction[0] == 0:
    print('\n\nThe person does NOT have a heart disease. Please note that this prediction system might not be accurate, proceed with caution!')
else:
    print('\n\nThe person has a heart disease. Please note that this prediction system might not be accurate, proceed with caution!')