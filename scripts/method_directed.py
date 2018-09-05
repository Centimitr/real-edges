def in_degree(g, node):
    return g.in_degree(node)


def out_degree(g, node):
    return g.out_degree(node)


def in_out_degree(g, node):
    node_in_degree = in_degree(g, node)
    node_out_degree = out_degree(g, node)
    result = node_in_degree / (node_out_degree + 1e-6)
    return result


def in_degree_a(g, a, b):
    return in_degree(g, a)


def in_degree_b(g, a, b):
    return in_degree(g, b)


def out_degree_a(g, a, b):
    return out_degree(g, a)


def out_degree_b(g, a, b):
    return out_degree(g, b)


def in_out_degree_a(g, a, b):
    return in_out_degree(g, a)


def in_out_degree_b(g, a, b):
    return in_out_degree(g, b)


def z1_b_to_a(g, a, b):
    for n in g.successors(b):
        if a == n:
            return 1
    return 0


def z2_middle(g, a, b):
    cnt = 0
    for n in g.successors(a):
        for nb in g.successors(b):
            if nb == n:
                cnt += 1
    return cnt


methods = [
    in_degree_a,
    in_degree_b,
    out_degree_a,
    out_degree_b,
    in_out_degree_a,
    in_out_degree_b,
    z1_b_to_a,
    z2_middle,
]

current = [
]
