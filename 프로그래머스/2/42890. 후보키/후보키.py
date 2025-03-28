from itertools import combinations 

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    
    combi = []
    for i in range(1,col+1) :
    	# 그냥 col하면 안되고 range(col)해야한다.
        # col까지의 숫자중에서 i개를 조합으로 뽑는다.
        combi.extend(combinations(range(col),i))
    # 유일성 
    unique = []
    for i in combi :
        tmp = [tuple(item[key] for key in i) for item in relation]
        if len(set(tmp)) == row :
            unique.append(i)
    # 최소성 
    answer = set(unique)
    for i in range(len(unique)) :
        for j in range(i+1, len(unique)) :
            # 부분집합이 있다면 
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])) :
                # 삭제 
                answer.discard(unique[j])
    return len(answer)