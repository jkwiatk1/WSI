# author: Jan Kwiatkowski
from sklearn.metrics import classification_report

from tree_draw import plot_tree
from model.decisionTree_id3 import ID3Tree
from model import dataPreparation

# cars dataSet
X_cars, y_cars = dataPreparation.preprocess_dataset(is_data_shuffle=False)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_cars, y_cars, test_size=0.2, random_state=20)

my_tree = ID3Tree(max_depth=1000, min_samples_split=2)
my_tree.fit(X_train, y_train)
dot = plot_tree(my_tree.root)
# print(dot.source)
dot.render('id3_tree', format='png', view=True)

y_pred = my_tree.predict(X_test)
print(classification_report(y_test, y_pred))
