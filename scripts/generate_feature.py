import sys
import time

import networkx as nx
import numpy as np
import pandas as pd


# class Counter:
#     def __init__(self, initial_value=0):
#         self.v = initial_value
#         return
#
#     def get(self):
#         cur = self.v
#         self.v += 1
#         return cur

class Config:
    def __init__(self, pairs_path, output_prefix):
        self.pairs_path = pairs_path
        self.output_prefix = output_prefix


class GenerateFeatureTask:
    def __init__(self, out_dir="", out_suffix=""):
        self.out_dir = out_dir
        self.out_suffix = out_suffix
        self.pairs = []
        self.pair_path = ""
        self.graph = None

    def load_pairs(self, path, max_rows=None):
        if self.pair_path != path:
            self.pairs = np.genfromtxt(path, usecols=(1, 2), skip_header=1, max_rows=max_rows, delimiter="\t")
            # self.pairs = np.genfromtxt(path, usecols=(0, 1), max_rows=max_rows, delimiter=" ")
            self.pair_path = path

    def load_graph(self, path):
        print("Graph: Loading")
        print(path)
        start = time.time()
        self.graph = nx.read_gpickle(path)
        end = time.time()
        print("Graph: Loaded in %ds" % int(end - start))
        print()

    def output_feature_to_file(self, pairs, feature_name, output_filename, fn):
        if self.graph is None:
            print("Error: graph not loaded.")

        heading = ['source', 'sink', feature_name]
        rows = [heading]
        total = len(pairs)
        print("Feature:", feature_name, total)
        p_start = time.time()
        for i, p in enumerate(pairs):
            [a_float, b_float] = p
            [a, b] = [str(int(a_float)), str(int(b_float))]
            # print("\r{:.2%}".format(float(i) / float(total)))
            if i % 100 == 0:
                sys.stdout.write('\r')
                # the exact output you're looking for:
                percent = (float(i * 100) / float(total))
                sys.stdout.write("%.2f%% %d/%d" % (percent, i, total))
                sys.stdout.flush()

            feature_value = fn(self.graph, a, b)
            rows.append([a, b, feature_value])
        p_end = time.time()
        print("Process: Finished in %ds" % int(p_end - p_start))
        print("Output:", feature_name)
        pd.DataFrame(data=rows).to_csv(output_filename, header=False)
        print("Complete:", feature_name)
        print()

    def output(self, prefix, fn):
        out_path = self.out_dir + "/" + "".join(
            [prefix, "_", fn.__name__, ".", self.out_suffix])
        self.output_feature_to_file(self.pairs, fn.__name__, out_path, fn)

    def load_and_output(self, config, fn):
        self.load_pairs(config.pairs_path)
        self.output(config.output_prefix, fn)

    def multi_load_and_output(self, configs, fns):
        for c in configs:
            self.load_pairs(c.pairs_path)
            for fn in fns:
                self.output(c.output_prefix, fn)
