import pandas as pd
import os


def getFileNamesWithPrefix(path, prefix):
    for (_, _2, names) in os.walk(path):
        return [n for n in names if n.startswith(prefix)]


path = "../out"
# prefix = "t_"
# prefix = "tp"
prefix = "pn"

result = None
for i, n in enumerate(getFileNamesWithPrefix(path, prefix)):
    file_path = path + "/" + n
    df = pd.read_csv(file_path)
    feature_name = list(df)[3]
    if i == 0:
        result = df
        df.columns = ['0', '_source', '_sink', feature_name]

    result[feature_name] = df[feature_name]

result.sort_index(axis=1, inplace=True)
result.to_csv(prefix + ".csv", index=False)
