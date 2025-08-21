import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn import metrics

df = pd.read_csv("W:/vscode/Machine-Learning/titanic.csv")
#print(df.head())

target = df["Survived"]
#print(target)

drop_df = df.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked","Survived"],axis="columns")
label_sex = LabelEncoder()
drop_df["label_sex"] = label_sex.fit_transform(drop_df["Sex"])
inputs = drop_df.drop(["Sex"],axis="columns")
inputs.Age = inputs.Age.fillna(inputs.Age.mean())
# print(inputs)
x_train, x_test, y_train, y_test = model_selection.train_test_split(inputs, target,test_size=0.2)
model = tree.DecisionTreeClassifier()

model.fit(x_train,y_train)

pred = model.predict(x_test)
# print(len(x_train))
# print(len(x_test))
print(metrics.accuracy_score(pred,y_test))

