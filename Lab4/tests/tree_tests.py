from sklearn import tree
from sklearn.datasets import  load_iris
from sklearn.tree import export_text
from sklearn.metrics import classification_report
from model.decisionTree_id3 import ID3Tree
from model import dataPreparation


# cars dataSet
X_cars,y_cars = dataPreparation.preprocess_dataset()

iris = load_iris()
X_iris, y_iris = iris.data, iris.target

print("Drzewo z biblioteki")
clf = tree.DecisionTreeClassifier(random_state=0, max_depth=1000)
clf = clf.fit(X_iris, y_iris)
tree.plot_tree(clf)
r = export_text(clf, feature_names=iris['feature_names'])
print(r)


#my tree
print("Moje drzewo")
my_tree = ID3Tree(max_depth = 1000, min_samples_split = 2)
my_tree = my_tree.fit(X_iris,y_iris)
# my_tree.fit(X_iris,y_iris)
# y_pred = my_tree.predict(X_iris)
# r2 = export_text(my_tree, feature_names=iris['feature_names'])
# print(r2)


# print(classification_report(y_iris, y_pred))
