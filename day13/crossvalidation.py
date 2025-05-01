import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.preprocessing import StandardScaler

# Load datasets
breast_cancer = load_breast_cancer()
iris = load_iris()

# Breast cancer features and target
x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Series(breast_cancer.target, name='target')

# Iris features and target
x_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
y_iris = pd.Series(iris.target, name='target')

# Breast cancer: Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Iris: Train-test split
x_train_iris, x_test_iris, y_train_iris, y_test_iris = train_test_split(x_iris, y_iris, test_size=0.2, random_state=42)

# Standardize features (without target column!)
scaler_bc = StandardScaler()
x_train = pd.DataFrame(scaler_bc.fit_transform(x_train), columns=x_train.columns)
x_test = pd.DataFrame(scaler_bc.transform(x_test), columns=x_test.columns)

scaler_iris = StandardScaler()
x_train_iris = pd.DataFrame(scaler_iris.fit_transform(x_train_iris), columns=x_train_iris.columns)
x_test_iris = pd.DataFrame(scaler_iris.transform(x_test_iris), columns=x_test_iris.columns)

# Train Random Forest on Breast Cancer
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)

# Predict and evaluate Breast Cancer
y_pred = rf.predict(x_test)
y_pred_proba = rf.predict_proba(x_test)[:, 1]

print(f"Breast Cancer Dataset - Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Breast Cancer Dataset - Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Breast Cancer Dataset - Recall: {recall_score(y_test, y_pred):.4f}")
print(f"Breast Cancer Dataset - F1 Score: {f1_score(y_test, y_pred):.4f}")
print(f"Breast Cancer Dataset - ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
print(f"Breast Cancer Dataset - Confusion Matrix:\n{pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])}")
print(f"Breast Cancer Dataset - Classification Report:\n{classification_report(y_test, y_pred)}")

# Train Random Forest on Iris
rf.fit(x_train_iris, y_train_iris)

# Predict and evaluate Iris
y_pred_iris = rf.predict(x_test_iris)

print(f"\nIris Dataset - Accuracy: {accuracy_score(y_test_iris, y_pred_iris):.4f}")
print(f"Iris Dataset - Precision: {precision_score(y_test_iris, y_pred_iris, average='weighted'):.4f}")
print(f"Iris Dataset - Recall: {recall_score(y_test_iris, y_pred_iris, average='weighted'):.4f}")
print(f"Iris Dataset - F1 Score: {f1_score(y_test_iris, y_pred_iris, average='weighted'):.4f}")
print(f"Iris Dataset - Confusion Matrix:\n{pd.crosstab(y_test_iris, y_pred_iris, rownames=['Actual'], colnames=['Predicted'])}")
print(f"Iris Dataset - Classification Report:\n{classification_report(y_test_iris, y_pred_iris)}")
