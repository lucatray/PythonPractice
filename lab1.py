#lab 1
def left(e):
    return e[0]
def operator(e):
    return e[1]             # These are the functions
def right(e):
    return e[2]


def isInside(v, e):
    if v == e:
        return True
    elif isInside(v, left(e)):  #booleans to see what part of the equation the variable is located
            return True
    elif isInside(v, right(e)):
        return True
    else:
        return False

def solve(v, q):
    if isInside(v, left(q)):
        return solving(v, q)
    elif isInside(v, right(q)):
        rightToLeft = (right(q), operator(q), left(q))    #method
        return solve(v, rightToLeft)
    else:
        return None

def solving(v, q):
    if v == left(q):
        return q
    elif operator(q) == '+':
        return solvingAdd(v, q)
    elif operator(q) == '-':
        return solvingSubtract
    elif operator(q) == '*':
        return solvingMultiply
    else:
        return solvingDivide




def solvingAdd(v, q):
    if isInside(v, left(left(q))):
        return (left(left(q)), '=', (right(q), '-', right(left(q)))) #
    else:
        return (left(right(q), '=', (right(q), '-', left(left(q)))))

def solvingSubtract(v, q):
    if isInside(v, left(left(q))):
        return (left(left(q)), '=', (right(q), '+', right(left(q)))) #
    else:
        return  (right(left(q)),'=',(right(left(q)),'-', right(q)))

def solvingMultiply(v,q):
    if isInside(v,left(left(q))):
        return (left(left(q)), '=', (right(q), '/',right(left(q)))) #
    else:
        return isInside(v,right(left(q)))

def solvingDivide(v, q):
    if isInside(v, left(left(q))):
        return (left(left(q)), '=', (right(q), '*', right(left(q))))
    else:
        return (right(left(q)), '=', (right(left(q)), '/', right(q)))

print(isInside('x', 'x'))                          #  True   1 point
print(isInside('x', 'y'))                          #  False  1 point
print(isInside('x', ('x', '+', 'y')))              #  True   2 points
print(isInside('x', ('a', '+', 'b')))              #  False  2 points
print(isInside('+', ('a', '+', 'b')))              #  False  2 points
print(isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points

print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points

print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points

