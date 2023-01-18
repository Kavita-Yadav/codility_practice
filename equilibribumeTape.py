def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    sum1 = A[0]
    #print('sum0-1:',sum1) 
    sum2 = sum(A) - A[0]
    #print('sum0-2:',sum2) 
    min_diff = abs(sum1-sum2)
    #print('min_diff0:',min_diff) 
    for i in range(1, N-1):
        print('->', i)
        sum1 += A[i]
        #print('sum1-1:',sum1) 
        sum2 -= A[i]
        #print('sum1-2:',sum2)
        #print('min_diff_abs:',abs(sum1 - sum2))
        min_diff = min(min_diff, abs(sum1 - sum2))
        #print('min_diff1:',min_diff)
    
    return min_diff
