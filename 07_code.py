import sys

sys.stdin = open("07_input.txt", "r", encoding="utf-8")


def solution():
    # 누적합 풀이방법
    def to_minute(n):
        h, m = map(int, n.split(":"))
        return h * 60 + m

    T = int(input())

    for i in range(T):
        N = int(input())
        book_time = [input().split() for _ in range(N)]

        bookings = [0] * 1451

        for start, end in book_time:
            start = to_minute(start)
            end = to_minute(end) + 10

            bookings[start] += 1  # 입실했으니 방 수 + 1
            bookings[end] -= 1    # 퇴실했으니 방 수 - 1

        answer = 0
        cur = 0

        for r in bookings:
            cur += r
            answer = max(answer, cur)

        print(answer)


solution()