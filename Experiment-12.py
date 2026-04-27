Python

from sklearn.naive_bayes import GaussianNB from sklearn.datasets import load_iris from sklearn.model_selection import train_test_split from sklearn.metrics import accuracy_score

data load_iris()

X_train, X_test, y_train, y_test train_test_split (data.data, data.target, test_size=0.3)

nb GaussianNB()

nb.fit(X_train, y_train)

print (f"Naive Bayes Accuracy: (accuracy_score (y_test, nb.predict (X_test)):.2f}")
Experiment 12
