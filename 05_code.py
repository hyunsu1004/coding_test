import sys

sys.stdin = open("05_input.txt","r",encoding="utf-8")

def solution():

    T = int(input())

    for i in range(T):
        directions = input().strip()
       
        ok = (('E' in directions) == ('W' in directions) and ('N' in directions) == ('S' in directions))

        if ok:
            print("YES")
        else:
            print("NO")

       




solution()