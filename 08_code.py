from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    n = len(queue1)
    arr = queue1 + queue2
    total  = sum(arr)
    #print(total)
    
    if total % 2 != 0:
        return -1
    
    target = total // 2
    cur = sum(queue1)
    p1,p2 = 0,n
    limit = n * 4
    arr = arr + arr #인덱스 초과 방지용
    
    count = 0
    
    while count <= limit:
        if cur == target:
            return count
        if cur > target:
            cur -= arr[p1]
            p1 += 1
        else:
            cur += arr[p2]
            p2 += 1
        count += 1
    
    
    
    return -1