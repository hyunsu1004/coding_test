def solution(k, tangerine):
    answer = 0
    
    count_type = {}
    
    n = len(tangerine)
    for i in range(n):
        if tangerine[i] not in count_type:
            count_type[tangerine[i]] = 1
        else:
            count_type[tangerine[i]] += 1
    
    count = []
    cnt = 0
    
    
    for key,value in count_type.items():
            count.append(value)
    
    count.sort(reverse=True)
    
    for i in count:
        k -= i
        answer += 1
        if k<=0:
            break
    
    return answer