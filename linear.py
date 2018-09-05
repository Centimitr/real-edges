import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# class Edges:
#     def __init__(self):
#         self.test_set = []
#         self.train_set = dict()
#         self.all_ids = set()
#         self.X_train = []
#         self.y_train = []
#         self.X_test = []
#         return
#
#     def load_test_set(self, path):
#         self.test_set = np.genfromtxt(path, dtype='int', delimiter='\t', skip_header=1)
#
#     def load_train_set(self, path):
#         with open(path) as f:
#             train_set = dict()
#             all_ids = set()
#             for l in f:
#                 ids = [int(s) for s in l.rstrip().split('\t')]
#                 cur, *following = ids
#                 all_ids = all_ids.union(ids)
#                 train_set[cur] = set(following)
#             f.close()
#             self.train_set = train_set
#             self.all_ids = all_ids
#
#     def generate_features(self):
#         return


# e = Edges()
# e.load_train_set('data/train.txt')
# e.load_train_set('data/small_train.txt')
# e.load_test_set('data/test-public.txt')

# print(len(e.all_ids))

# regr = linear_model.LinearRegression()
# regr.fit(e.X_train, e.y_train)
# y_pred = regr.predict(e.X_test)
#
# # The coefficients
# print('Coefficients: \n', regr.coef_)
# # The mean squared error
# # print("Mean squared error: %.2f"
# #       % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# # # Explained variance score: 1 is perfect prediction
# # print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))
#
# # Plot outputs
# # plt.scatter(e.X_test, diabetes_y_test, color='black')
# plt.plot(e.X_test, y_pred, color='blue', linewidth=3)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()
