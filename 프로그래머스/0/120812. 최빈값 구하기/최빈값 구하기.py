from collections import defaultdict
def solution(array):
    answer = 0
    count_dict = defaultdict(int)
    
    for num in array:
        count_dict[num] += 1
    data = list(sorted(count_dict.items(), key=lambda x: -x[1]))
    
    if len(data) > 1 and data[0][1] == data[1][1]: return -1
	
    return data[0][0]