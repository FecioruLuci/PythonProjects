import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn import tree



df = pd.read_csv("W:/vscode/Machine-Learning/salaries.csv")

inputs = df.drop("salary_more_then_100k", axis= "columns")
target = df["salary_more_then_100k"]
#print(inputs)

label_company = LabelEncoder()
label_job = LabelEncoder()
label_degree = LabelEncoder()

inputs["label_company"] = label_company.fit_transform(inputs["company"])
inputs["label_job"] = label_job.fit_transform(inputs["job"])
inputs["label_degree"] = label_degree.fit_transform(inputs["degree"])
#print(inputs.head())

n_inputs = inputs.drop(["company","job","degree"],axis="columns")
#print(n_inputs.head())

model = tree.DecisionTreeClassifier()
model.fit(n_inputs,target)

pred = model.predict([[2,2,1]])
print(pred)