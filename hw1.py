# Homework 1 for CS161 -- Quincy McCall (505 894 780)

def PAD(n):
    # takes in a single integer n and returns the value of the
    
    # nth integer in the Padovan sequence
    
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return PAD(n-2) + PAD(n-3)

# Overall, this solution recursively builds the Padovan sequence by calling PAD on the n-2 and n-3 
# integers in the sequence until it is called on 0,1, or 2 which return the value 1
# and then sums the returning values, ultimately returning the value of n.

# Assertions used for testing:
#assert PAD(0) == 1, "assertion 1 failed"
#assert PAD(1) == 1, "assertion 2 failed"
#assert PAD(2) == 1, "assertion 3 failed"
#assert PAD(3) == 2, "assertion 4 failed"
#assert PAD(4) == 2, "assertion 5 failed"
#assert PAD(5) == 3, "assertion 6 failed"
#assert PAD(14) == 37, "assertion 7 failed"
#print("all tests passed!")


def SUMS(n):
    # takes in one parameter, a single integer n 
    
    # returns a single integer that is the count of additions to get to the nth number
    
    if n == 0 or n==1 or n==2:
        return 0
    else:
        return 1 + SUMS(n-2) + SUMS(n-3)
    
# Overall this solution recursively calls SUMS on the n-2 and n-3 characters until SUMS is called on 
# 0,1, or 2 which returns the value 0 and then sums together all of the returning values + 1 
# and ultimately returns the number of additions required to get to the nth number in the sequence

# Assertions used for testing: 
#assert SUMS(0) == 0, "assertion 1 failed"
#assert SUMS(1) == 0, "assertion 2 failed"
#assert SUMS(2) == 0, "assertion 3 failed"
#assert SUMS(3) == 1, "assertion 4 failed"
#assert SUMS(4) == 1, "assertion 5 failed"
#assert SUMS(5) == 2, "assertion 6 failed"
#assert SUMS(6) == 3, "assertion 7 failed"
#assert SUMS(14) == 36, "assertion 8 failed"
#print("all tests passed!")

def ANON(tree):
    
    # takes a single nested tuple representation of a tree as the argument
    
    # and returns the same structure with every leaf node turned into "?"
    
    if type(tree) is tuple:
        return tuple(ANON(subtree) for subtree in tree)
    else:
        return "?"
    
# Overall this function checks if the type is a tuple and if so it recursively calls ANON on every subtree 
# in the tuple and if it reaches a leaf node, converts its value to a "?", once all leaf nodes have 
# been converted the function returns a nested tuple of the same structure with all leaf nodes now equal 
# to "?"

# Assertions used for testing:       
#assert ANON(((("L", "E"), "F"), "T")) == ((("?", "?"), "?"), "?"), "assertion failed 1"
#assert ANON((5, "FOO", 3.1, -0.2))==("?", "?", "?", "?"), "assertion failed 2"
#assert ANON((1, ("FOO", 3.1), -0.2))== ("?", ("?", "?"), "?"), "assertion failed 3"
#assert ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2)))==((("?", "?"), ("?", "?")), ("?", "?")), "assertion failed 4"
#assert ANON(("R", ("I", ("G", ("H", "T")))))==("?", ("?", ("?", ("?", "?")))), "assertion failed 5"
#assert ANON(42) =="?", "assertion failed 6"
#assert ANON("FOO")== "?", "assertion failed 7"
#print("all tests passed!")
