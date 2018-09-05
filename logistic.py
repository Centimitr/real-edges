import csv

from sklearn.linear_model import LogisticRegression
import numpy as np

# features_path = "data/f3.txt"
# test_path = "data/test-public.txt"

# tp_path = "X1.csv"
# pn_path = "X2.csv"
# t_path = "X3.csv"
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

tp_path = "out_combined/tp.csv"
pn_path = "out_combined/pn.csv"
t_path = "out_combined/t_.csv"

# rng = (4, 6, 14)  # 0.75505, 0.6753
# rng = (3, 6)  # 0.77909, 0.6743
# rng = (3, 6, 10)  # 0.78365, 0.6729

# rng = (3, 6, 10, 16)

rng = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

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

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=666)

X_train, y_train = X, y
X_test = XT

clf = LogisticRegression(C=1)
clf.fit(X_train, y_train)

pred = clf.predict_proba(X_test)

# roc = roc_auc_score(y_test, pred[:, 1])
# print(roc)

# print()
# for v in pred[:, 1]:
# print(v)

with open('pred.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['Id', 'Prediction'])
    for i, p in enumerate(pred[:, 1]):
        w.writerow([i + 1, p])

print(np.mean(pred[:, 1]))
