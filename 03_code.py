import sys

sys.stdin = open("03_input.txt","r",encoding="utf-8")

def solution():
    T = int(input())
    #print(T)
    number = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
    #8만 2개 , 1은 가장 작은수 0
    #만약 3이면 80, 5이면, 808 , 짝수면 무조건 88

    for tc in range(T):
        N = int(input())

        if N == 1:
            print(0)

        elif N % 2 == 0:
            print(int("8" * (N//2)))

        else:
            print(int("4" + "8" * ((N-1)//2)))

    return 


solution()