import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def output_pred(path, pred):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['Id', 'Prediction'])
        for i, p in enumerate(pred[:, 1]):
            w.writerow([i + 1, p])


def train_and_pred(rng, test=False):
    tp_path = "out_combined/tp.csv"
    pn_path = "out_combined/pn.csv"
    t_path = "out_combined/t_.csv"

    X1 = np.genfromtxt(tp_path, usecols=rng, skip_header=1, delimiter=",")
    X2 = np.genfromtxt(pn_path, usecols=rng, skip_header=1, delimiter=",")
    XT = np.genfromtxt(t_path, usecols=rng, skip_header=1, delimiter=",")

    print(X1.shape)
    print(X2.shape)
    print(XT.shape)

    y1 = np.ones(len(X1))
    y2 = np.zeros(len(X2))

    X = np.concatenate((X1, X2))
    y = np.concatenate((y1, y2))

    y_test = None
    if test:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=90054)
    else:
        X_train, y_train = X, y
        X_test = XT

    clf = LogisticRegression(C=1)
    clf.fit(X_train, y_train)

    pred = clf.predict_proba(X_test)

    if y_test is not None:
        roc = roc_auc_score(y_test, pred[:, 1])
        print(roc)
        print()

    return pred


def train_and_test(rng):
    return train_and_pred(rng, True)


def calc_pred_mean(pred):
    print(np.mean(pred[:, 1]))
