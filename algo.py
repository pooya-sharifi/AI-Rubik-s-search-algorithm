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
        cost_limit = 1
        nodes = 0
        moves = list()
        frontier_start = OrderedDict()
        frontier_goal = OrderedDict()
        solved = solved_state()

        print(init_state)
        print("Bi-BFS")

        start = Node()
        start.cube = init_state
        frontier_start[hash(start.cube.tobytes())] = start
        goal = Node()
        goal.cube = solved
        frontier_goal[hash(goal.cube.tobytes())] = goal
        while len(frontier_start) != 0 and len(frontier_goal) != 0:
            # Forward search from start
            key_start, curr_start = frontier_start.popitem(last=False)

        
            if hash(curr_start.cube.tobytes()) in frontier_goal:
                # The two searches meet
                curr_goal = frontier_goal[hash(curr_start.cube.tobytes())]
                print("Meet in the middle")
                # Retrieve moves from the initial state to the meeting point
                backing = frontier_goal[hash(curr_start.cube.tobytes())]
                front = curr_start
                moves_start = []
                while front.parent is not None:
                    print(front.cube)
                    moves_start.append(front.move)
                    front = front.parent
                    print("move_1 start",moves_start)
                    print("move_1 parent",front.cube)

                

                moves_start.reverse()
                # print("move_1 start",moves_start)

                # Retrieve moves from the meeting point to the goal state
                moves_goal = []
                while backing.parent is not None:
                    print(backing.cube)
                    if(backing.move >6):
                        moves_goal.append(backing.move-6)
                    else:
                        moves_goal.append(backing.move+6)
                    backing = backing.parent
                    # print("parent cube when backing",backing.cube,backing.move)
                    print("move_2 start",moves_goal)
                    print("move_2 parent",backing.cube)
                    

                # moves_goal.reverse()
                # print("move_2 start",moves_goal)

                # check
                
                
                # Combine the two series of moves
                # moves_goal.reverse()
                moves = moves_start + moves_goal
                # moves.reverse()

                print("test_begin",start.cube)
                test_start=start.cube
                for i in range(4):
                    second=Node()
                    print(moves[i])
                    second.cube = next_state(test_start, moves[i])
                    print("test",second.cube)
                    test_start=second.cube

                
                return moves
                
                # Further processing if needed
                break
            if curr_start.cost + 1 <= cost_limit:
                child_cost = curr_start.cost + 1
                for i in range(12):
                    nodes += 1
                    new_start = Node()
                    new_start.cube = next_state(curr_start.cube, i + 1)
                    new_start.cost = child_cost
                    new_start.parent = curr_start
                    new_start.move = i + 1
                    frontier_start[hash(new_start.cube.tobytes())] = new_start
                # print("start toward goal")

            # Backward search from goal
            key_goal, curr_goal = frontier_goal.popitem(last=False)

            if hash(curr_goal.cube.tobytes()) in frontier_start:
                # The two searches meet
                curr_start = frontier_start[hash(curr_goal.cube.tobytes())]
                print("Meet in the middle_2")
                # Further processing if needed
                # backing = frontier_start[hash(curr_goal.cube.tobytes())]
                # front = curr_goal
                front = frontier_start[hash(curr_goal.cube.tobytes())]
                backing = curr_goal
                moves_start = []
                while front.parent is not None:
                    print(curr_start.cube)
                    moves_start.append(front.move)
                    front = front.parent
                    print("move_1 start",moves_start)
                # print(curr_start.cube)

                moves_start.reverse()
                # print("move_1 start",moves_start)

                # Retrieve moves from the meeting point to the goal state
                moves_goal = []
                while backing.parent is not None:
                    # print(backing.cube)
                    print("move_2 start",backing.move)

                    if(backing.move >6):
                        moves_goal.append(backing.move-6)
                    else:
                        moves_goal.append(backing.move+6)
                    # moves_goal.append(backing.move)
                    backing = backing.parent
                    # print("parent cube when backing",backing.cube,backing.move)
                    print("move_2 start",moves_goal)
                # moves_goal.reverse()
                # print("move_2 start",moves_goal)

                    

                # Combine the two series of moves
                # moves_goal.reverse()
                moves = moves_start + moves_goal
                # moves.reverse()
                
                return moves

            if curr_goal.cost + 1 <= cost_limit:
                child_cost = curr_goal.cost + 1
                for i in range(12):
                    nodes += 1
                    new_goal = Node()
                    new_goal.cube = next_state(curr_goal.cube, i + 1)
                    new_goal.cost = child_cost
                    new_goal.parent = curr_goal
                    new_goal.move = i + 1
                    frontier_goal[hash(new_goal.cube.tobytes())] = new_goal
                # print("goal toward start")

            cost_limit += 1


        return 0
    
    else:
        return []