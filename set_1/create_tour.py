# Eulerian Tour Ver 1
#
# Write a function, `create_tour` that takes as
# input a list of nodes
# and outputs a list of tuples representing
# edges between nodes that have an Eulerian tour.
#
import random

def create_tour_basic(nodes):
    # your code here
    res = []
    length = len(nodes)
    for i in range(length):
        res.append([nodes[i], nodes[(i+1) % length]])
    return res

def create_tour(nodes):
    # your code here
    unconnected = nodes.copy()
    connected = []
    res = []
    degree = {}
    x = pop_randomly(unconnected)
    y = pop_randomly(unconnected)
    degree[x] = 1
    degree[y] = 1
    res.append([x, y])
    connected.append(x)
    connected.append(y)
    while len(unconnected) > 0:
        x = pick_randomly(connected)
        y = pop_randomly(unconnected)
        res.append([x, y])
        degree[x] += 1
        degree[y] = 1 
    print ("Degree %s" % degree)
    odd_nodes = [k for k, v in degree.items() if v % 2 == 1]
    even_nodes = [k for k, v in degree.items() if v % 2 == 0]
    print ("First part %s" % res)
    while len(odd_nodes) > 0:
        print ("Oddd nodes %s" % odd_nodes)
        print ("Even nodes %s" % even_nodes)
        x = pop_randomly(odd_nodes)
        y = find_node(x, odd_nodes, res)
        if y is not None:
            even_nodes.append(x)
            even_nodes.append(y)
        else:
            y = find_node(x, even_nodes, res)
            even_nodes.append(x)
            odd_nodes.append(y)
        print ("Secon part %s" % res)

    return res
def critical_part(odd_nodes, even_nodes, res):
    x = pop_randomly(odd_nodes)
    y = find_node(x, odd_nodes, res)
    if y is not None:
        even_nodes.append(x)
        even_nodes.append(y)
    else:
        y = find_node(x, even_nodes, res)
        even_nodes.append(x)
        odd_nodes.append(y)
    print ("Oddd nodes %s" % odd_nodes)
    print ("Even nodes %s" % even_nodes)
    print ("Secon part %s" % res)  

def find_node(xnode, nodes, tour):
    for ynode in nodes:
        #print ("X Node %s, Y Node %s" % (xnode, ynode))
        if [xnode, ynode] in tour or [ynode, xnode] in tour:
            continue
        else:
            tour.append([xnode, ynode])
            nodes.remove(ynode)
            return ynode
    return None
    

def pick_randomly(nodes):
    i = random.randrange(0, len(nodes))
    return nodes[i]

def pop_randomly(nodes):
    i = random.randrange(0, len(nodes))
    return nodes.pop(i)
#########

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print ("Node %s has odd degree" % node)
                return False
        except KeyError:
            print ("Node %s was not in your tour" % node)
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print ("Your graph wasn't connected")
        return False

def test():
    nodes = [20, 21, 22, 23, 24, 25]
    tour = create_tour(nodes)
    return is_eulerian_tour(nodes, tour)

