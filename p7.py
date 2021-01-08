import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import csv

heartDisease=pd.read_csv('Data7.csv')
heartDisease=heartDisease.replace('?',np.nan)


print('few examples from the dataset are given below')
print('heartDisease.head()')

model=BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang',
'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),
('heartdisease','thalach'), ('heartdisease','chol')])


model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
HeartDisease_infer = VariableElimination(model)

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 37, 'sex' :0})
print(q['heartdisease'])

q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 100})
print(q['heartdisease'])
