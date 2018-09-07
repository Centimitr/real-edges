import csv
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


def output_pred(path, pred):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['Id', 'Prediction'])
        for i, p in enumerate(pred[:, 1]):
            w.writerow([i + 1, p])


def read_input(rng, test=False):
    tp_path = "out_combined/tp.csv"
    pn_path = "out_combined/pn.csv"
    t_path = "out_combined/t_.csv"

    X1 = np.genfromtxt(tp_path, usecols=rng, skip_header=1, max_rows=999999, delimiter=",")
    X2 = np.genfromtxt(pn_path, usecols=rng, skip_header=1, max_rows=999999, delimiter=",")
    XT = np.genfromtxt(t_path, usecols=rng, skip_header=1, delimiter=",")

    print(X1.shape)
    print(X2.shape)
    print(XT.shape)

    y1 = np.ones(len(X1))
    y2 = np.zeros(len(X2))

    X = np.concatenate((X1, X2))
    y = np.concatenate((y1, y2))

    # scaler = preprocessing.StandardScaler()
    # scaler_param = scaler.fit(X)
    # X = scaler.fit_transform(X, scaler_param)

    y_test = None
    if test:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=666)
    else:
        X_train, y_train = X, y
        X_test = XT

    return X_train, X_test, y_train, y_test, X, y


def train(X, y):
    clf = LogisticRegression(C=1.0)
    # clf = RandomForestRegressor(max_depth=2, random_state=0)
    clf.fit(X, y)
    # print("importance:", clf.feature_importances_)
    return clf


def train_and_pred(rng, test=False):
    X_train, X_test, y_train, y_test, X, y = read_input(rng, test)

    clf = train(X_train, y_train)
    pred = clf.predict_proba(X_test)
    # pred = clf.predict(X_test)

    if y_test is not None:
        print("clf.score: %.5f" % clf.score(X_test, y_test))
        # print("cross_val.5: ", cross_val_score(clf, X, y, cv=5))
        print("roc: %.5f" % roc_auc_score(y_test, pred[:, 1]))
        print("pred.mean: %.5f" % np.mean(pred[:, 1]))
        print()

    return pred


def train_and_test(rng):
    return train_and_pred(rng, test=True)
