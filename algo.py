import numpy as np
from state import next_state, solved_state
from location import next_location
from collections import OrderedDict



def solve(init_state, init_location, method):
    """
    Solves the given Rubik's cube using the selected search algorithm.
 
    Args:
        init_state (numpy.array): Initial state of the Rubik's cube.
        init_location (numpy.array): Initial location of the little cubes.
        method (str): Name of the search algorithm.
 
    Returns:
        list: The sequence of actions needed to solve the Rubik's cube.
    """

    # instructions and hints:
    # 1. use 'solved_state()' to obtain the goal state.
    # 2. use 'next_state()' to obtain the next state when taking an action .
    # 3. use 'next_location()' to obtain the next location of the little cubes when taking an action.
    # 4. you can use 'Set', 'Dictionary', 'OrderedDict', and 'heapq' as efficient data structures.
    class Node:
        cube = None
        cost = 0
        parent = None
        move = None

    if method == 'Random':
        return list(np.random.randint(1, 12+1, 10))
    
    elif method == 'IDS-DFS':
        cost_limit = 1
        nodes = 0
        moves=list()
        # frontier = list()
        frontier = OrderedDict()
        solved=solved_state()
        print(init_state)
        print("IDS-DFS")

        # for f in range(2):
        while True:
            start= Node()
            start.cube=init_state
            # frontier.append(start)
            frontier[hash(start.cube.tobytes())] = start

            

            while len(frontier) != 0:
            # for k in range(4):
                curr=Node()
                print(np.size(frontier))
                # print("frontier 0 balaye curr",frontier[0].curr)
                # curr = frontier.pop(0)
                key, curr = frontier.popitem(last=False)
                
                print(np.size(frontier))

                # print("curr",curr.cube)
                    # if goal_reached(curr.cube):
                    #     print('Goal Height:', curr.cost)
                    #     print('Branching Factor:', sum(branching_factors)/len(branching_factors))
                    #     # while curr is not None:
                    #     #    if curr.move is not None:
                    #     #        print(curr.move)
                    #     #    curr = curr.parent
                    #     print("Nodes Generated:", nodes)
                    # return
                # print(curr.cube[1])
                if (curr.cube[1] == [0,0]).all() :
                    print("okayyy")
                # print("solved",solved)
                if ((curr.cube==solved).all()):
                    node_search=curr
                    print("solved ones",curr.cube)
                    while(node_search.parent != None):
                        print("while success",node_search.parent.cube)
                        node_search=node_search.parent
                    node_search=curr
                    while(node_search.move != None):
                        print("while success move",node_search.move)
                        moves.append(node_search.move)
                        node_search=node_search.parent
                    moves.reverse()
                    print("success", moves)
                    return moves
                    
                    # print("costs",curr.cost,cost_limit)
                if curr.cost + 1 <= cost_limit:
                    child_cost = curr.cost + 1
                    b = 0

                    for i in range(12):
                        nodes = nodes + 1
                        new = Node()
                        # new.cube = np.array(curr.cube)
                        new.cube = next_state(curr.cube, i + 1)
                    
                        new.cost = child_cost
                        new.parent = curr
                        new.move = i + 1
                        # # if curr.parent is not None and np.array_equal(curr.parent.cube, new.cube):
                        # if curr.parent is not None and (contains1(new.cube, curr) or contains2(new.cube, frontier)):
                        #     continue
                        # frontier.append(new)
                        frontier[hash(new.cube.tobytes())] = new


                        # print("new",new.cube)
                        # print("frontier0",frontier[0].cube)
                        # b = b + 1
                    # branching_factors.append(b)
                # for node in frontier.values():
                #     print(node.cube)
                # branching_factors.clear()
                cost_limit = cost_limit + 1
        return list(np.random.randint(1, 12+1, 10))
    
    elif method == 'A*':
        ...

    elif method == 'BiBFS':
        ...
    
    else:
        return []