import generate_feature as gf
import method_undirected as mud
import method_directed as md
import combine_csv as ccsv

# tp_c = gf.Config("../train/tp_pairs_20000.csv", "tp")
# pn_c = gf.Config("../train/pn_pairs_20000.csv", "pn")
tp_c = gf.Config("../train/true_edge.csv", "tp")
pn_c = gf.Config("../train/false_edge.csv", "pn")
t_c = gf.Config("../train/test-public.txt", "t")
all_c = [tp_c, pn_c, t_c]


def generate_feature_csv():
    t = gf.GenerateFeatureTask(out_dir="../out_single", out_suffix="csv")

    t.load_graph("udg.gpickle")
    t.multi_load_and_output([pn_c, t_c], mud.methods)
    t.multi_load_and_output([tp_c], [mud.common_neighbour, mud.local_path])

    # t.load_graph("dg.gpickle")
    # t.multi_load_and_output(all_c, md.methods)


def main():
    generate_feature_csv()
    ccsv.multi_combine_csv("../out_single", "../out_combined", ["pn", "tp", "t_"])
    return


# generate_feature_csv()
# ccsv.multi_combine_csv("../out_single", "../out_combined", ["pn", "tp", "t"])
# ccsv.scale("../out_combined", "../out_combined_scaled")


if __name__ == "__main__":
    main()
