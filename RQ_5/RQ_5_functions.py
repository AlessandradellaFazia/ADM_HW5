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
    This function evaluate the distance between two class evaluating the mean of the shortest path 
    for each pair of the nodes in the sub graph cosisting of the nodes belonging to two different class.
    If the sets of nodes belonging to two different class are not linked by any edge, 
    we consuder the distance between infinite.
    '''
    
    Class_distance = dict()
    
    edges_C0 = Graph.subgraph(categories[C0]).edges
    
    for C in tqdm(category_dic.keys()):
        
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