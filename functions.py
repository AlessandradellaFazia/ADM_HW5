import operator
from tqdm import tqdm
import numpy as np

def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def BFS(Graph, Source, adj_list):
    
    '''
    In this function we implemented the breadth first search algorithm in order to evaluate the distance, 
    from a source node, of all the node in the graph.
    If a node is not linked to any other nodes it dosn't appeare in the dictionary called distance.
    '''
    
    # initialization
    distance = dict()
    visited = {k: False for k in Graph.nodes}
    queue = []

    queue.append(Source)
    distance[Source] = 0
    visited[Source] = True

    while queue:
        v = queue.pop()
        
        # check if the node has a list of first neighbors
        if v in adj_list.keys(): 
            
            # evaluate the distance and add new nodes to the queue
            for node in adj_list[v]:
                if visited[node] == False:
                    visited[node] = True
                    distance[node] = distance[v] + 1
                    queue.append(node)

    return distance

def Adjacency_list(Graph):
    
    '''
    In this function returnt the adjacency list, a dictionary in which to every node is associated
    an array of first neighbors nodes. It's take in imput a networkx graph object.
    '''
    
    List = dict()
    
    for source, destination in Graph.edges:
        
        if source not in List.keys():
            List[source] = []
        List[source].append(destination)    
    
    return List    


def Class_Distance(Graph, C0, categories):
    
    '''
    This function evaluate the distance between two class computing the mean of the shortest path 
    for each pair of the nodes in the sub graph consisting of the nodes belonging to two different classes.
    if there are no edges between nodes belonging to two different classes, we set the distance between infinite.
    '''
    
    Class_distance = dict()
    
    edges_C0 = Graph.subgraph(categories[C0]).edges
    
    for C in tqdm(categories.keys()):
        
        if C != C0:
            
            edges_C = Graph.subgraph(categories[C]).edges
            sub_Graph = Graph.subgraph(categories[C0] + categories[C])

            connected = []
            
            #check if there is at least one link between sets of nodes belonging to two different class
            for edge in sub_Graph.edges():
                if edge not in edges_C0 and edge not in edges_C:
                    connected.append(True)
            
            # evaluate shortest path between each pair using using repeated breadth first search
            if connected:
                distance = []
                adj_list = Adjacency_list(sub_Graph)

                for node in adj_list.keys():
                    d = BFS(sub_Graph, node, adj_list)
                    distance += [d[k] for k in d.keys() if d[k]!= 0]

                Class_distance[C] = np.mean(distance)

            else:
                Class_distance[C] = float('inf')
                
    return Class_distance

def Nearest_page(graph, source, num_click, adj_list):
    distance = BFS(graph, source, adj_list)
    return [k for k in distance.keys() if distance[k] <= num_click]


def min_clicks(graph, category, list_of_pages, input_edges, output_edges):
    
    pagedegree_dict = {}
    
    pageclicks_dict = {}
    
    tot_links = len(input_edges) #numero totale di in-links del graph
    
    for page in list_of_pages:
        
        page = int(page)
        
        if page in input_edges.keys():
                  
             #Calcolo della Deg_Centrality associata ad ogni pagina passata in INPUT
            
            n_inlinks = len(input_edges[page]) #numero di in-links associati al nodo "page"
            
            
            in_degree_centrality = n_inlinks/tot_links 
            
            pagedegree_dict[page] = in_degree_centrality
    
    max_indegree_centr = max(pagedegree_dict.values())  # maximum value
    page_with_max_indegree_centr = max(pagedegree_dict.items(), key=operator.itemgetter(1))[0]
    
    page_clicks_dict = {}
    
    distance = BFS(graph, page_with_max_indegree_centr,output_edges)
    
    for page in list_of_pages:
            
        if page in distance.keys() and page != page_with_max_indegree_centr:
            
            n_clicks = distance[page] #number of clicks associated to the current page
            page_clicks_dict[page] = n_clicks
    
    page_clicks_dict = dict(sorted(page_clicks_dict.items(),
                           key=lambda item: item[1],
                           reverse=False))
            
    return page_clicks_dict

def min_cuts(G, source, target, path = []):
    
    path = path + [source]
    n_cuts = 0
    
    if source == target:
        return [path]
        
    if source not in G.nodes():
        print("non c'è il nodo source")
        return []
        
    paths = []
    
    for node in G[source]:
            
        if node not in path:
        
            newpaths = [min_cuts(G, node, target, path)]
                
            for newpath in newpaths:
                n_cuts += 1
                
    return n_cuts