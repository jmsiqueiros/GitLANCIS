import networkx as nx
import argparse
import scipy as sp

#open the edgelist file of an original mental model
edgelist = open(arg.edgelist)
mapper = open(arg.mapper)
output_edgelist = arg.outputedgelist

#Creates a network from input edgelist
g = nx.read_edgelist(edgelist, delimiter=',')

#Relabels in a new network
h = nx.relabel_nodes(g, mapper)

#Writes a file with the standardized terms network
nx.write_edgelist(h, output_edgelist, delimiter=',')

#Returns graph adjacency matrix
a = nx.adjacency_matrix(h)
