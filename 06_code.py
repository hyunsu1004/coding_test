import sys

sys.stdin = open("06_input.txt","r",encoding="utf-8")


def solution():
    T = int(input())

    for i in range(T):
        N = int(input())
        word = input().strip()

        stack = []

        for ch in word:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
                stack.pop()
                stack.pop()
                stack.pop()

        print(len(stack))

    

solution()