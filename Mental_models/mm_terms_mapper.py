import networkx as nx
import numpy as np
import argparse
import scipy as sp
import pylab as pl
import json

parser = argparse.ArgumentParser(description='It changes the nodes labels of mental models with a list of standard labels for terms.')
parser.add_argument('--dictionary', type=argparse.FileType('r'), required=True, help="Feed a json file with the mapping equivalences")
parser.add_argument('--network', type=argparse.FileType('r'), required=True, help="Input a network.csv to which nodes names will be relabeled")
parser.add_argument('--out_edgelist', type=str, required=True, help="Give me a name for your edgelist out_edgelist.csv file")
parser.add_argument('--out_matrix', type=str, help="Give me a name for your adjacency matrix out_matrix.csv file")
args    = parser.parse_args()


#mapping = {'liquido':'agua','desecho':'basura'}
mapping = json.load(args.dictionary) 


#Creates a network from input edgelist
g = nx.read_edgelist(args.network, delimiter=',')


#Relabels in a new network
h = nx.relabel_nodes(g, mapping)

nx.draw(h)
pl.show()

#Writes a file with the standardized terms network
nx.write_edgelist(h, args.out_edgelist, delimiter=',')

#Returns graph adjacency matrix
a = nx.adjacency_matrix(h)
np.savetxt(args.out_matrix, a, delimiter=",")
