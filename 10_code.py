def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d = p = 0
    #d: 아직 배달하지 못한 상자의 누적 개수 (음수면 트럭에 여유 용량이 남았다는 뜻)
    #p : 아직 수거하지 못한 빈 상자의 누적 개수
    for i in range(n-1,-1,-1): #n-1부터 0까지 -1씩
        d += deliveries[i] 
        p += pickups[i]
        while d > 0 or p > 0: #배달이든 수거든 하나라도 남아있으면 트럭이 이 집(i)까지 가야함
            d -= cap
            p -= cap
            answer += (i+1) * 2
    return answer