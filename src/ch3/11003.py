# 11003
'''
문제:
N개의 수 A1, A2, ..., AN과 L이 주어진다.
Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

입력:
첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
둘째 줄에는 N개의 수 A_i가 주어진다. (-10^9 ≤ Ai ≤ 10^9)

출력:
첫째 줄에 D_i를 공백으로 구분하여 순서대로 출력한다.
'''

from collections import deque
n, l = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(n):
    # mydeque[-1][0]: 마지막 deque의 값
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    # mydeque[0][1]: 첫번째 deque의 인덱스, i - l: 현재 윈도우의 첫번째 인덱스
    if mydeque[0][1] <= i - l:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
