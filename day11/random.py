import pandas as pd
from sklearn.datasets import load_iris,load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn.tree import _tree
import matplotlib.pyplot as plt
iris=load_iris()
boston=load_boston()
X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)
clf=DecisionTreeClassifier(random_state=42)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
X_train,X_test,y_train,y_test=train_test_split(boston.data,boston.target,test_size=0.2,random_state=42)
reg=DecisionTreeRegressor(random_state=42)
reg.fit(X_train,y_train)
y_pred=reg.predict(X_test)
print("MSE:",mean_squared_error(y_test,y_pred))
def plot_tree(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    plt.figure(figsize=(20, 10))
    plt.title("Decision Tree")
    _ = tree.plot_tree(
        tree,
        feature_names=feature_name,
        filled=True,
        rounded=True,
        fontsize=14
    )
    plt.show()
plot_tree(clf, iris.feature_names)
plot_tree(reg, boston.feature_names)
