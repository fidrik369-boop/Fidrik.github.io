Program:

Python

from sklearn.ensemble import RandomForestClassifier from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris

from sklearn.metrics import accuracy_score

data load iris()

X train, X_test, y_train, y_test train_test_split (data.data,

data.target, test_size=0.3)

rf RandomForestClassifier(n estimators=100)

rf.fit (X_train, y_train)

y_pred rf.predict (X_test)

print (f"Random Forest Accuracy: (accuracy_score (y_test, y_pred):.2f)")
