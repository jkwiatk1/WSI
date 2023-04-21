from matplotlib import pyplot as plt

from model.dataPreparation import preprocess_dataset
from sklearn.model_selection import train_test_split
from model.randomForest import RandomForest
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

NB_TREES = 25
X_cars,y_cars = preprocess_dataset(is_data_shuffle=True,sort_by_last_column=False)

print('test for 15% test, 85% train')
X_train_015, X_test_015, y_train_015, y_test_015 = train_test_split(X_cars, y_cars, test_size=0.15, random_state=20)
rf_3 = RandomForest(n_trees= NB_TREES)
rf_3.fit(X_train_015, y_train_015)
y_pred_015 = rf_3.predict(X_test_015)

rf_3_conf_mat = ConfusionMatrixDisplay.from_estimator(rf_3,X_test_015,y_test_015)
rf_3_conf_mat.plot(cmap=plt.cm.Blues)
plt.show()
print('\nAccuracy: {:.2f}\n'.format(accuracy_score(y_test_015, y_pred_015)))
print('Micro Precision: {:.2f}'.format(precision_score(y_test_015, y_pred_015, average='micro')))
print('Micro Recall: {:.2f}'.format(recall_score(y_test_015, y_pred_015, average='micro')))
print('Micro F1-score: {:.2f}\n'.format(f1_score(y_test_015, y_pred_015, average='micro')))
print(classification_report(y_test_015, y_pred_015))



