from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.datasets import load_iris

# Load Dataset
data = load_iris()

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

# Base Model
dt = DecisionTreeClassifier()

# Parameter Tuning
params = {
    'max_depth': [2, 4, 6, 8],
    'criterion': ['gini', 'entropy']
}

grid = GridSearchCV(dt, params, cv=5)

grid.fit(X_train, y_train)

print(f"Best Parameters: {grid.best_params_}")
print(f"Best Score: {grid.best_score_:.2f}")
