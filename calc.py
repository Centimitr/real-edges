import csv

import numpy as np

import logistic as lr

# rng = (4, 6, 14)  # 0.75505, 0.6753
# rng = (3, 6)  # 0.77909, 0.6743
# rng = (3, 6, 10)  # 0.78365, 0.6729

# rng = (3, 6, 10)

# rng = (3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17)
rng = (3, 4, 5, 6, 7, 8, 9)
pred = lr.train_and_pred(rng)
# pred = lr.train_and_test(rng)
lr.output_pred('out_pred/pred.csv', pred)
