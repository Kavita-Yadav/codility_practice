def solution(N):
    decTobin = bin(N).replace("0b", "")
    # bin_value = "{0:b}".format(int(45))
    prev_count = 0
    count = 1 #4
    prev_value = ''
    gap = []
    for i in decTobin:
        current_value = i
        if current_value == "0":
            if current_value == prev_value:
                count = count+1
            else:
                prev_value = current_value
                prev_count = count
        else:
            if(current_value == "1" and prev_value == "0"):
                prev_value = current_value
                gap.append(count)
                prev_count=0
                count = 1
            else:
                gap.append(0)
        
    return max(gap)
