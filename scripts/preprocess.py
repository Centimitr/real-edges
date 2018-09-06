# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in
import csv

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
from random import randint


def generate_dataset(train_path, test_path, output_path):
    vertex_set = set()
    sink_dict = {}

    with open(train_path) as trainfile:
        for i, line in enumerate(trainfile):
            line_list = [int(k) for k in line[:-1].split("\t")]
            vertex_set.add(line_list[0])
            for s in line_list[1:]:
                if s in sink_dict:
                    sink_dict[s] += 1
                else:
                    sink_dict[s] = 1
            if i % 1000 == 0:
                print(i)

    print(len(sink_dict))
    print(len(vertex_set))

    new_sink_dict = {}
    threshold = 10
    for k in sink_dict:
        if sink_dict[k] >= threshold:
            new_sink_dict[k] = sink_dict[k]

    new_sink_set = set(new_sink_dict)
    print(len(new_sink_set))

    test_vertex_and_sink_set = set()

    with open(test_path) as testfile:
        for i, line in enumerate(testfile):
            if i == 0:
                continue
            line_list = [int(k) for k in line[:-1].split("\t")]
            for s in line_list:
                test_vertex_and_sink_set.add(s)
    print(len(test_vertex_and_sink_set))

    total_set = test_vertex_and_sink_set.union(new_sink_set).union(vertex_set)
    print(len(total_set))

    total_dict = {}
    total_list = []
    for i, p in enumerate(total_set):
        total_dict[p] = i
        total_list.append(p)
    print(total_dict[4394015])
    print(total_dict[2397416])
    print(total_dict[1272125])
    print(total_dict[2984819])
    print(total_list[83517])
    print(total_list[124658])
    print(total_list[93341])
    print(total_list[348183])

    max_neighbors = 1000

    import numpy as np

    total_array = np.array(total_list)

    pairs = []

    with open(train_path) as trainfile:
        for i, line in enumerate(trainfile):
            line_list = [int(k) for k in line[:-1].split("\t")]
            v = line_list[0]
            ranking = [-sink_dict[k] for k in line_list[1:]]
            sorting = np.argsort(ranking)
            filtered_linelist = np.array(line_list[1:])[sorting]
            for s in filtered_linelist[1:max_neighbors]:
                if s in total_set:
                    pairs.append([total_dict[v], total_dict[s]])
            if i % 1000 == 0:
                print(i)

    test_pairs = []

    with open(test_path) as testfile:
        for i, line in enumerate(testfile):
            if i == 0:
                continue
            line_list = [int(k) for k in line[:-1].split("\t")]
            test_pairs.append([line_list[0], total_dict[line_list[1]], total_dict[line_list[2]]])

    np.savez_compressed(output_path, correspondence=total_array, pairs=pairs, test_pairs=test_pairs)

    print(os.path.getsize(output_path + '.npz') / 1000000)


def load_set(path):
    with np.load(path) as fd:
        return fd['pairs']


def generate_tp(source_path, path, limit):
    prs = load_set(source_path)

    with open(path, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['Id', 'Source', 'Sink'])
        for i in range(20000):
            idx = randint(0, len(prs) - 1)
            p = prs[idx]
            w.writerow([i + 1, p[0], p[1]])
            if i + 1 >= limit:
                return


def convert_simple_train_file(in_path, out_path):
    pairs = np.genfromtxt(in_path, usecols=(0, 1), delimiter=" ")
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['Id', 'Source', 'Sink'])
        for i, pr in enumerate(pairs):
            w.writerow([i + 1, pr[0], pr[1]])


# generate_dataset("../data/train.txt", "../data/test-public.txt", "../out_data/filtered_data")
#
# generate_tp('../out_data/filtered_data.npz', '../train/tp_pairs_20000.csv', 20000)

convert_simple_train_file("../train/false_edge.txt", "../train/false_edge.csv")
convert_simple_train_file("../train/true_edge.txt", "../train/true_edge.csv")
