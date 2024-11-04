##############
# Homework 2 #
##############

##############
# Question 1 #
##############
def BFS(FRINGE):
    # The BFS function takes in a single nested tuple, FRINGE, as its input 
    # The function returns a list of elements in FRINGE in BFS order
    
    next_level = []
    bfs_list = []
    
    for fringe_element in FRINGE:
        if type(fringe_element) is tuple:
            next_level.extend(fringe_element)
        else:
            bfs_list.append(fringe_element)
            
    if next_level:
        return bfs_list + BFS(next_level)
    else:
        return bfs_list

# The overall solution of BFS is to check for each element in FRINGE if it is a tuple, and if it is
# then it adds it to the next level list, and if it is not a tuple it adds it to the bfs_list,
# #the BFS function is then recursively called with the next level list and added to the bfs_list and
# ultimately returns the list of elements in BFS order

# Test Cases
# assert BFS(("A",)) == ['A'], "Test case 1 failed"
# assert BFS(((("X", "Y"), "Z"),)) == ['Z', 'X', 'Y'], "Test case 2 failed"
# assert BFS((("1", ("2", ("3", "4")), "5"),)) == ['1', '5', '2', '3', '4'], "Test case 3 failed"
# assert BFS((("P", ("Q", "R"), ("S", "T", "U")),)) == ['P', 'Q', 'R', 'S', 'T', 'U'], "Test case 4 failed"
# assert BFS((("X", ("Y", ("Z",)))),) == ['X', 'Y', 'Z'], "Test case 5 failed"
# assert BFS((("M", ("N", ("O", ("P",))), "Q"),)) == ['M', 'Q', 'N', 'O', 'P'], "Test case 6 failed"
# assert BFS(("ROOT",)) == ['ROOT']
# assert BFS((((("L", "E"), "F"), "T"))) == ['T', 'F', 'L', 'E']
# assert BFS((("R", ("I", ("G", ("H", "T")))))) == ['R', 'I', 'G', 'H', 'T']
# assert BFS(((("A", ("B",)), "C", ("D",)))) == ['C', 'A', 'D', 'B']
# assert BFS((("T", ("H", "R", "E"), "E"))) == ['T', 'E', 'H', 'R', 'E']
# assert BFS((("A", (("C", (("E",), "D")), "B")))) == ['A', 'B', 'C', 'D', 'E']

# print("All tests passed!")







##############
# Question 2 #
##############


# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS returns [].
# To call DFS to solve the original problem, one would call
# DFS((False, False, False, False), [])
# However, it should be possible to call DFS with a different initial
# state or with an initial path.

# First, we define the helper functions of DFS.

# FINAL-STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    # This function takes in a single argument S that represents the current state
    # The function returns True if S is the goal state and False otherwise
    
    return S == (True, True, True, True)


# NEXT-STATE returns the state that results from applying an operator to the
# current state. It takes three arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns None.
# NOTE that next-state returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].

def NEXT_STATE(S, A):
    # This function takes in two arguments, S and A, S represents the current state and
    # A represents what move is being made, either homer alone = "h", homer and baby = "b"
    # homer and dog = "d", or homer and poison = "p"
    # the function returns a list of only valid successor states
    # (homer, baby, dog, poison)
    
    result = list(S)
    # homer and baby to move
    if A == "b":
        # check if homer and baby are on the same side
        if S[0] != S[1]:
            return None
        # change homer and baby to opposite side
        result[0] = not S[0]
        result[1] = not S[1]
    #homer to move alone
    elif A == "h":
        # change homer to opposite side
        result[0] = not S[0]
    #homer and dog to move
    elif A == "d":
        # check if homer and dog are on the same side
        if S[0] != S[2]:
            return None
        # change homer and dog to opposite side
        result[0] = not S[0]
        result[2] = not S[2]
    # homer and poison to move
    elif A == "p":
        # check if homer and poison are on the same side
        if S[0] != S[3]:
            return None
        # change homer and poison to opposite side
        result[0] = not S[0]
        result[3] = not S[3]
    # if homer is on the goal side 
    if result[0] == True:
        # check if the baby and poison or the baby and the dog are alone on the opposite side
        if result[1] == False and result[2] == False or result[1] == False and result[3] == False:
            return None
    # if homer is on the not goal side
    elif result[0] == False:
        # check if the baby and poison or the baby and the dog are alone on the opposite side
        if result[1] == True and result[2] == True or result[1] == True and result[3] == True:
            return None
    # return the list of only valid successor states
    return [tuple(result)]

# SUCC-FN returns all of the possible legal successor states to the current
# state. It takes a single argument (s), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    # This function takes in a single argument S that represents the current state
    # The function returns a list of all the successor states
    successor_states = []
    moves = ["h", "b", "d", "p"]
    for move in moves:
        next_state = NEXT_STATE(S, move)
        if next_state:
            successor_states.append(next_state[0])
    return successor_states



# ON-PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if s is a member of
# states and False otherwise.
def ON_PATH(S, STATES):
    # This function takes in two arguments, S, the current state, and STATES which is the stack 
    # of states visited by DFS
    # The function returns True if S is on the stack of states visited by DFS
    return S in STATES




# MULT-DFS is a helper function for DFS. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT-DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT-DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    # this function takes in two arguments, STATES, which is a list of successor states 
    # to the current state, and PATH, which is the path from the initial state to the current state
    # this function returns the complete path from the initial state to the goal state by recursively calling DFS

    # run on all successor states in STATES
    for state in STATES:
        # check if state is the goal state
        if FINAL_STATE(state):
            # if state is the goal state, return the path with the goal state added
            return PATH + [state]
        
        # if state is not the goal state, run DFS on state
        result = DFS(state, PATH)
        if result:
            return result
    return []


# DFS does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path.
def DFS(S, PATH):
    # This function takes in two arguments, S, the current state, and PATH, which is the path
    # from the initial state to S, not including S
    # The function returns the path from the initial state to the goal state, if any, or [] otherwise
    
    # check if S is the goal state
    if FINAL_STATE(S):
        return PATH + [S]
    # check if S has already been visited
    if ON_PATH(S, PATH):
        return []
    # add S to the path
    PATH = PATH + [S]
    # get the successors of S
    successors = SUCC_FN(S)
    # call Mult-DFS on successors of S, with S appended to the path
    return MULT_DFS(successors, PATH)

# Test Cases 
#  assert DFS((False, False, False, False), []) == [
#         (False, False, False, False),
#         (True, True, False, False),
#         (False, True, False, False),
#         (True, True, True, False),
#         (False, False, True, False),
#         (True, False, True, True),
#         (False, False, True, True),
#         (True, True, True, True)
#     ]
# assert DFS((True, True, True, True), []) == [
#         (True, True, True, True)
#     ]
# assert DFS((True, True, False, False), []) == [
#         (True, True, False, False),
#         (False, True, False, False),
#         (True, True, True, False),
#         (False, False, True, False),
#         (True, False, True, True),
#         (False, False, True, True),
#         (True, True, True, True)
#     ]
# assert DFS((False, False, True, True), [
#     (False, False, False, False), 
#     (True, True, False, False), 
#     (False, True, False, False), 
#     (True, True, True, False), 
#     (False, False, True, False), 
#     (True, False, True, True)]) == [
#         (False, False, False, False), 
#         (True, True, False, False), 
#         (False, True, False, False), 
#         (True, True, True, False), 
#         (False, False, True, False), 
#         (True, False, True, True), 
#         (False, False, True, True), 
#         (True, True, True, True)]
  
# print("passed DFS test")