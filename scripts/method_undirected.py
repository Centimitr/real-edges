import collections
import itertools

import networkx as nx


def util_count_iter_items(iterable):
    counter = itertools.count()
    collections.deque(itertools.izip(iterable, counter), maxlen=0)
    return next(counter)


def common_neighbour(g, a, b):
    cn = nx.common_neighbors(g, a, b)
    return len(list(cn))
    # return util_count_iter_items(cn)


def adamic_adar_index(g, a, b):
    aa = nx.adamic_adar_index(g, [(a, b)])
    for u, v, p in aa:
        return p


def preferential_attachment(g, a, b):
    aa = nx.preferential_attachment(g, [(a, b)])
    for u, v, p in aa:
        return p


def resource_allocation(g, a, b):
    aa = nx.resource_allocation_index(g, [(a, b)])
    for u, v, p in aa:
        return p


def jaccard_coefficient(g, a, b):
    aa = nx.jaccard_coefficient(g, [(a, b)])
    for u, v, p in aa:
        return p


def summation_neighbours(g, a, b):
    return g.degree(a) + g.degree(b)


def local_path(g, a, b):
    # 1266s
    alpha = 0.01

    source_neighbors = []
    for n in nx.neighbors(g, a):
        source_neighbors.append(n)
    nn = []
    for n in source_neighbors:
        nn.append(nx.neighbors(g, n))
    sink_neighbors = []
    for n in nx.neighbors(g, b):
        sink_neighbors.append(n)

    count1 = 0
    count2 = 0
    for x in sink_neighbors:
        if x in source_neighbors:
            count1 = count1 + 1
        if x in nn and x not in source_neighbors:
            count2 = count2 + 1

    lp = count1 + alpha * count2
    return lp


def z0_shortest_path(g, a, b):
    path = nx.shortest_path(g, a, b)
    if len(path) > 6:
        return 6
    return len(path)


# methods = [
#     common_neighbour,
#     adamic_adar_index,
#     preferential_attachment,
#     resource_allocation,
#     jaccard_coefficient,
#     summation_neighbours,
#     local_path,
#     # z0_shortest_path
# ]

methods = [
    adamic_adar_index,
    preferential_attachment,
    resource_allocation,
    jaccard_coefficient,
    summation_neighbours,
    common_neighbour,
    local_path,
    # z0_shortest_path
]
