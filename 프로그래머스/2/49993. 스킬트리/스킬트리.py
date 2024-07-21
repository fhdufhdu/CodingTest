def solution(skill, skill_trees):
    answer = 0
   	
    for skill_tree in skill_trees:
        removed = "".join([st for st in skill_tree if st in skill])
       	
        check = True
        for i in range(min(len(skill), len(removed))):
            if skill[i] != removed[i]: 
                check = False
                break
        if check:
        	answer += 1
        
    return answer