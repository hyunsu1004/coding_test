import sys

sys.stdin = open("04_input.txt","r",encoding="utf-8")


def solution():
    T = 10

    for i in range(1,T+1):

        N= int(input())
        arr = list(map(int,input().split()))
        cnt = 0
        for j in range(2,N-2):
            compare = arr[j-2:j] + arr[j+1:j+3] #좌우 2칸씩
            highest = max(compare)

            if arr[j] > highest: #비교하는 값이 가장 높은 빌딩이라면
                cnt += arr[j] - highest
            else:
                continue

        print(f"{T} {cnt}")

solution()

