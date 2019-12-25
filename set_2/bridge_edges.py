# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       
def create_rooted_spanning_tree(G, root):
    S = {}
    for xnode in G.keys():
        if xnode not in S:
            S[xnode] = {}
        for ynode in G[xnode].keys():
            if ynode not in S[xnode].keys():
                if reached (S, xnode, ynode):
                    S[xnode][ynode] = 'red'
                else:
                    S[xnode][ynode] = 'green'
    return S

def reached(S, node1, node2):
    reached = [node1]
    openlist = [node1]
    while len(openlist) > 0:
        current = openlist.pop(0)
        if current in S:
            for node in S[current].keys():
                if node not in reached:
                    if node == node2:
                        return True
                    else:
                        reached.append(node)
                        openlist.append(node)
    return False

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, 'a')
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    mapping = {}
    index = 1
    openlist = [root]
    while len(openlist) > 0:
        currentLen = len(openlist)
        current = openlist[currentLen -1]
        for node in S[current].keys():
            if node not in openlist and node not in mapping.keys() and S[current][node] == 'green':
                openlist.append(node)
        if currentLen == len(openlist):
            mapping[current] = index
            index += 1
            del openlist[currentLen -1]
    return mapping

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    mapping = {}
    openlist = [root]
    while len(openlist) > 0:
        currentLen = len(openlist)
        current = openlist[currentLen -1]
        number_of_descendants = 0
        for node in S[current].keys():
            if node not in openlist and node not in mapping.keys() and S[current][node] == 'green':
                openlist.append(node)
            if node in mapping.keys() and S[current][node] == 'green':
                number_of_descendants += mapping[node]
        if currentLen == len(openlist):
            mapping[current] = number_of_descendants +1
            del openlist[currentLen -1]
    return mapping

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    mapping = {}
    po_modified = po.copy()
    openlist = [root]
    while len(openlist) > 0:
        currentLen = len(openlist)
        current = openlist[currentLen -1]
        for node in S[current].keys():
            if node not in openlist and node not in mapping.keys():
                openlist.append(node)
        if len(openlist) == currentLen:
            mapping[current] = min(po_modified[value] for value in S[current].keys())
            mapping[current] = min(mapping[current], po_modified[current])
            po_modified[current] = mapping[current]
            del openlist[currentLen -1]
    return mapping

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    mapping = {}
    po_modified = po.copy()
    openlist = [root]
    while len(openlist) > 0:
        current = openlist.pop()
        mapping[current] = max(po_modified[value] for value in S[current].keys())
        mapping[current] = max(mapping[current], po_modified[current])
        po_modified[current] = 0
        for node in S[current].keys():
            if node not in openlist and node not in mapping.keys() and S[current][node] == 'green':
                openlist.append(node)
    return mapping

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    result = []
    S = create_rooted_spanning_tree(G, 'a')
    po = post_order(S, 'a')
    nd = number_of_descendants(S, 'a')
    lowest = lowest_post_order(S, 'a', po)
    highest = highest_post_order(S, 'a', po)
    # for each 'green' edge check second node for
    # highest <= po
    # lowest > po - nd
    openlist = ['a']
    processed = []
    while len(openlist) > 0:
        current = openlist.pop()
        processed.append(current)
        for node in S[current].keys():
            if S[current][node] == 'green':
                if node not in openlist and node not in processed:
                    openlist.append(node)
                if node not in processed and highest[node] <= po[node] and lowest[node] > (po[node] - nd[node]):
                    result.append((current, node))  
    return result

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]
