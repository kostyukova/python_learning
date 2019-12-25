import down_heapify_tuple

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Write centrality to return the avarage distance
# from a node to all the other nodes it can reach
def centrality (G, v):
    distance = {}
    openlist = [v]
    distance[v] = 0
    while len(openlist) > 0:
        current = openlist.pop(0)
        for neibor in G[current].keys():
            if neibor not in distance:
                distance[neibor] = distance[current] + 1
                openlist.append(neibor)
    return (sum(distance.values()) + 0.0)/len(distance)


def test_ports():
    flights = [("ORD", "SEA"), ("ORD", "LAX"), ('ORD', 'DFW'), ('ORD', 'PIT'),
               ('SEA', 'LAX'), ('LAX', 'DFW'), ('ATL', 'PIT'), ('ATL', 'RDU'),
               ('RDU', 'PHL'), ('PIT', 'PHL'), ('PHL', 'PVD')]

    G = {}
    port_centrality = {}
    for (x, y) in flights:
        make_link(G, x, y)
    print G
    for (x, y) in flights:
        if x not in port_centrality:
            port_centrality[x] = centrality(G, x)
        if y not in port_centrality:
            port_centrality[y] = centrality(G, y)
    print port_centrality

    top_k = 3
    heap = []
    func = lambda x : x[1]
    for port, value in port_centrality.items():
        if len(heap) < top_k:
            heap.insert(0, (port, value))
            down_heapify_tuple.down_heapify(heap, 0, func)
        else:
            if value > func(heap[0]):
                down_heapify_tuple.push_min(heap, (port, value), func)
        print heap
    

def test_actors():
    file = open("imdb-4.tsv", "r")
    for line in file:
        (name, movie, year) = line.rsplit("\t")