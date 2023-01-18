# time complexity O(n**n)
def solution(A):
    # write your code in Python 3.6
    # list comprehension and list.count(element)
    # list.count(element) helps to count that specific element appear how many times in list
    # if current item of list appeared(count) once in a list then it is unpaired item
    uniqueInt = list([x for x in A if A.count(x) == 1])
    # use unpaired_item_list[0] to return ony on item, remove position/index to return whole list of items
    return uniqueInt[0]
  
 OR

def solution(A):
  unpaired_item_list = []
  for i in A:
    if A.count(i) == 1:
      unpaired_item_list.append(i)
      
  return unpaired_item_list[0]


OR

# Best solution with time complexity O(N) or O(N*log(N)) 

def solution(A):
    N = len(A)
    unpaired = 0
    
    for i in range(0, N):
        unpaired = unpaired ^ A[i]
    
    return unpaired
