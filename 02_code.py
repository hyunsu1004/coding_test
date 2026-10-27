import sys

sys.stdin = open("02_input.txt","r",encoding="utf-8")

def solutions():
    T = int(input())
    print(T)
    for tc in range(1,T+1):
        N = int(input())
        maps = [[0]*N for _ in range(N)]
        #오른쪽,아래,왼쪽,위 순으로
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]

        r,c,d = 0,0,0
        for num in range(1,N*N+1):
            maps[r][c] = num
            nr,nc = r + dr[d], c + dc[d] #처음엔 오른쪽으로
            if not (0<=nr<N and 0<=nc<N) or maps[nr][nc] != 0:
                d = (d+1) % 4
                nr,nc = r + dr[d], c + dc[d]
            r,c = nr,nc

        print(f"#{tc}")
        for row in maps:
            print(*row)
        #print(maps)


solutions()