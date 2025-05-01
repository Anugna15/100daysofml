import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, StratifiedKFold, LeaveOneOut, LeavePOut
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# Load dataset
breast_cancer = load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

# Scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Initialize model
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Helper function to perform cross-validation
def cross_validate(model, X, y, cv_method):
    accuracies = []
    precisions = []
    recalls = []
    f1_scores = []
    
    for train_idx, test_idx in cv_method.split(X, y):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracies.append(accuracy_score(y_test, y_pred))
        precisions.append(precision_score(y_test, y_pred))
        recalls.append(recall_score(y_test, y_pred))
        f1_scores.append(f1_score(y_test, y_pred))
    
    return np.mean(accuracies), np.mean(precisions), np.mean(recalls), np.mean(f1_scores)

# 1. K-Fold Cross Validation
print("\n---- K-Fold CV ----")
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
acc, prec, rec, f1 = cross_validate(rf, X, y, kfold)
print(f"Accuracy: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1-Score: {f1:.4f}")

# 2. Stratified K-Fold Cross Validation
print("\n---- Stratified K-Fold CV ----")
stratkfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
acc, prec, rec, f1 = cross_validate(rf, X, y, stratkfold)
print(f"Accuracy: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1-Score: {f1:.4f}")

# 3. Leave-One-Out Cross Validation
print("\n---- Leave-One-Out CV ----")
loo = LeaveOneOut()
# Warning: Very slow for large datasets
acc, prec, rec, f1 = cross_validate(rf, X, y, loo)
print(f"Accuracy: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1-Score: {f1:.4f}")

# 4. Leave-P-Out Cross Validation (P=2)
print("\n---- Leave-P-Out (P=2) CV ----")
lpo = LeavePOut(p=2)
# Warning: Extremely slow for large datasets. We'll run it on a small subset!
small_X = X[:50]
small_y = y[:50]
acc, prec, rec, f1 = cross_validate(rf, small_X, small_y, lpo)
print(f"Accuracy (on small set): {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f} | F1-Score: {f1:.4f}")
