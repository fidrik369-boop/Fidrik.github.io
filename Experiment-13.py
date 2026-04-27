from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Dataset
data = load_iris()

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

# Create and Train SVM Model
svm_model = SVC(kernel='linear')

svm_model.fit(X_train, y_train)

# Predict and Evaluate
y_pred = svm_model.predict(X_test)

print(f"SVM Accuracy: {accuracy_score(y_test, y_pred):.2f}")
