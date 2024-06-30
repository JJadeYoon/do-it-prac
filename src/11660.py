# 11660
'''
문제:
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오.
(x, y)는 x행 y열을 의미한다.

입력:
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다.
둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다.
다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다.
표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

출력:
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)

