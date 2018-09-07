import pandas as pd
import os


def getFileNamesWithPrefix(path, prefix):
    for (_, _2, names) in os.walk(path):
        return [n for n in names if n.startswith(prefix)]


def combine_csv(in_path, out_path, prefix):
    result = None
    for i, n in enumerate(getFileNamesWithPrefix(in_path, prefix)):
        file_path = in_path + "/" + n
        df = pd.read_csv(file_path)
        feature_name = list(df)[3]
        if i == 0:
            result = df
            df.columns = ['0', '_source', '_sink', feature_name]

        result[feature_name] = df[feature_name]

    result.sort_index(axis=1, inplace=True)
    result.to_csv(out_path + "/" + prefix + ".csv", index=False)


def multi_combine_csv(in_path, out_path, prefices):
    for p in prefices:
        combine_csv(in_path, out_path, p)

    # def scale(path, out_path):
    #     names = getFileNamesWithPrefix(path, "")
    #     scaler = StandardScaler()
    #     for n in names:
    #         file_path = path + "/" + n
    #         df = pd.read_csv(file_path)
    #         headings = list(df)
    #         print(headings[3:])
    #         for h in headings[3:]:
    #             df[h] = scaler.fit_transform(df[h], scaler.fit(df[h]))
    #             print()
    #         df.to_csv(out_path + "/" + n, index=False)

    # multi_combine_csv("../out_single", "../out_combined", ["pn", "tp", "t"])


# multi_combine_csv("../out_single", "../out_combined", ["pn", "tp", "t_"])
