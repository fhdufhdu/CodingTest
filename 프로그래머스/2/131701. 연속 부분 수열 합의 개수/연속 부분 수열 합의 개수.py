from itertools import permutations
def solution(elements):
    answer = 0
    """
    7, 9, 1, 1, 4
    16, 10, 2, 5, 11
    17, 11, 6, 12, 20
    """ 
    ne = [e for e in elements]
   	
    s = set(ne)
    for i in range(1, len(elements)):
        nne = []
        for j in range(len(elements)):
            prev_idx = (i+j) % len(elements)
            nne.append(elements[prev_idx]+ne[j])
        ne = nne
        for n in nne:
        	s.add(n)
    answer = len(s)
    return answer