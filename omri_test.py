from matplotlib import pyplot as plt
import networkx as nx
import torch

from pmc import pmc


def unify_complete_and_uniform_graphs(k, n, p=0.5):
    # Create a complete graph of size k
    complete_graph = nx.complete_graph(k)
    # return complete_graph
    random_graph = G = nx.gnp_random_graph(n, p)
    return nx.compose(complete_graph, random_graph)



# Example usage
k = 30  # Size of the complete graph
n = 200  # Total size of the unified graph
p = 0.7
DATASET_SIZE = 1000


def generate():
    unified_graph = unify_complete_and_uniform_graphs(k, n, p)
    unified_graph = unified_graph.to_directed()

    # use pmc to find the maximum clique of the unified graph
    ei = []
    ej = []
    for edge in unified_graph.edges:
        ei.append(edge[0])
        ej.append(edge[1])
    number_of_nodes = max(n, k)
    number_of_edges = len(ei)
    max_clique = pmc(ei, ej, max(n, k), len(ei))
    return {
        "graph": unified_graph,
        "max_clique_size": len(max_clique),
        "k": k,
        "n": n,
        "number_of_edges": number_of_edges,
        "number_of_nodes": number_of_nodes,
    }


dataset = [generate() for _ in range(DATASET_SIZE)]
print("finished generating dataset")
torch.save(dataset, f"./datasets/g_{n}_{p}_hidden_{k}.pt")
print("finished")
