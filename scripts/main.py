import generate_feature as gf
import method_undirected as mud
import method_directed as md

tp_c = gf.Config("../train/tp_pairs_20000.csv", "tp")
pn_c = gf.Config("../train/pn_pairs_20000.csv", "pn")
t_c = gf.Config("../train/test-public.txt", "t")
all_c = [tp_c, pn_c, t_c]

t = gf.GenerateFeatureTask(out_dir="../out", out_suffix="csv")
t.load_graph("udg.gpickle")
# t.load_graph("dg.gpickle")

# t.multi_load_and_output([tp_c, t_c], [md.z1_b_to_a, md.z2_middle])
# t.multi_load_and_output([pn_c], md.methods)
# t.multi_load_and_output(all_c, md.methods)
t.multi_load_and_output([pn_c], mud.methods)
