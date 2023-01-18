import math
def solution(X, Y, D):
    Distance = Y-X
    Jump = Distance/D
    
    return math.ceil(Jump)

