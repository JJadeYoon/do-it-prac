# 17298
'''
문제:
크기가 N인 수열 A = A1, A2, ..., AN이 있다.
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
그러한 수가 없는 경우에 오큰수는 -1이다.

입력:
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력:
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
'''

import sys

input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))

# 초기화
ans = [0] * N
my_stack = []

# 반복
for i in range(N):
    while my_stack and A[my_stack[-1]] < A[i]:
        ans[my_stack.pop()] = A[i]
    my_stack.append(i)

while my_stack:
    ans[my_stack.pop()] = -1

result = ""

for i in range(N):
    result += str(ans[i]) + " "

print(result)
