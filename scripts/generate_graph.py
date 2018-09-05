import networkx as nx
import linecache

# generate a graph
# G = nx.Graph()
G = nx.DiGraph()
count = len(open('train.txt', 'r').readlines())  # count rows in train.txt
cnt = 0
pair = [['source', 'sink']]

while cnt < count:
    row = linecache.getline('train.txt', cnt)
    row = row.strip('\n')
    row = row.split("\t")
    G.add_nodes_from(row)

    for i in range(1, len(row)):
        G.add_edge(row[0], row[i])  # add edges to graph
        pair.append([row[0], row[i]])
        i += 1

    print("Row ", cnt + 1)
    cnt += 1

# nx.write_gpickle(G, "udg.gpickle")
nx.write_gpickle(G, "dg.gpickle")
