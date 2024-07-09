# 1377
'''
문제:
버블 정렬의 swap이 한번도 일어나지 않은 루프가 언제인지 알아내자.

입력:
첫째 줄에 N이 주어진다. N은 500,000보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 A[1]부터 A[N]까지 하나씩 주어진다.
A에 들어있는 수는 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력:
정답을 출력
'''

import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    # 데이터의 순서가 정렬의 우선순위이다.
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max + 1)