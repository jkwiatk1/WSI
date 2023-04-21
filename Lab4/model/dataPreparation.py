import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_dataset(is_data_shuffle = False,sort_by_last_column = False):
    df = pd.read_csv("../database/car.data", header=None, delimiter=',')
    df.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

    if sort_by_last_column:
        df = df.sort_values(df.columns[-1])

    if is_data_shuffle == True:
        df = df.sample(frac=1)
    ydf = df[[df.columns[-1]]]

    df.drop(df.columns[-1], axis=1, inplace=True)
    xdf = df

    # One hot encoding
    xdf = pd.get_dummies(data=xdf, columns=['buying', 'maint', 'lug_boot', 'safety'])
    xdf['doors'].replace('5more', '5', inplace=True)
    xdf['persons'].replace('more', '5', inplace=True)
    # Conversion to numeric values
    xdf = xdf.apply(pd.to_numeric)

    le = LabelEncoder()
    ydf = le.fit_transform(ydf.values.ravel())

    X, y = xdf.values, ydf
    return X, y
