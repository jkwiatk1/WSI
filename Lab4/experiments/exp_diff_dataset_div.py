from model.dataPreparation import preprocess_dataset
from sklearn.model_selection import train_test_split
from model.randomForest import RandomForest
from sklearn.metrics import classification_report
import evaluate.evaluator

NB_TREES = 25
X_cars,y_cars = preprocess_dataset(is_data_shuffle=False)


# test for 5% test, 95% train
X_train_005, X_test_005, y_train_005, y_test_005 = train_test_split(X_cars, y_cars, test_size=0.05, random_state=20)
rf_1 = RandomForest(n_trees= NB_TREES)
rf_1.fit(X_train_005, y_train_005)
y_pred_005 = rf_1.predict(X_test_005)
print(classification_report(y_test_005, y_pred_005))

# test for 10% test, 90% train
X_train_01, X_test_01, y_train_01, y_test_01 = train_test_split(X_cars, y_cars, test_size=0.1, random_state=20)
rf_2 = RandomForest(n_trees= NB_TREES)
rf_2.fit(X_train_01, y_train_01)
y_pred_01 = rf_2.predict(X_test_01)
print(classification_report(y_test_01, y_pred_01))

# test for 15% test, 85% train
X_train_015, X_test_015, y_train_015, y_test_015 = train_test_split(X_cars, y_cars, test_size=0.15, random_state=20)
rf_3 = RandomForest(n_trees= NB_TREES)
rf_3.fit(X_train_015, y_train_015)
y_pred_015 = rf_3.predict(X_test_015)
print(classification_report(y_test_015, y_pred_015))

# test for 20% test, 80% train
X_train_02, X_test_02, y_train_02, y_test_02 = train_test_split(X_cars, y_cars, test_size=0.2, random_state=20)
rf_4 = RandomForest(n_trees= NB_TREES)
rf_4.fit(X_train_02, y_train_02)
y_pred_02 = rf_4.predict(X_test_02)
print(classification_report(y_test_02, y_pred_02))