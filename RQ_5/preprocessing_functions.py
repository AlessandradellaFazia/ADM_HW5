import random
import networkx as nx

def Build_inverted_dictionary(file, seed = 54557):
    
    '''
    this function build the inverted index in wich each node is linked to the list of categories it belong.
    In case of more than one category select only one of them
    '''
        
    #building the inverted dictionary
    inverted_dic = dict()
    f = open(file, encoding='utf-8')
    for line in f.readlines():
        Category, Nodes = line.replace('Category:', '').split(';')

        for node in map(int, Nodes.strip().split()):
            if node not in inverted_dic:
                inverted_dic[node] = list()
            inverted_dic[node].append(Category)

    f.close()
    
    # select only one category for each node
    random.seed(seed)
    for k in inverted_dic.keys():
        chosen = random.choice(inverted_dic[k])
        inverted_dic[k] = chosen
    
    return inverted_dic

def Build_graph(file, nodes):
    ''' 
    this function, given a set of nodse and edges, return a netvorkx graph object.
    '''
        
    DG = nx.DiGraph()
    
    DG.add_nodes_from(nodes)  # add nodes
    
    f = open(file)
    f.readline()
    
    # add edges
    for line in f.readlines():
        idx, source, destination = map(int, line.strip().split('\t'))
        
        DG.add_edge(*(source, destination))
    
    return DG 