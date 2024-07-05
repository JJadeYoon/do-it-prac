# 12891
'''
문제:
임의의 DNA 문자열과 비밀번호로 사용할 부분분자열의 길이, 그리고 {‘A’, ‘C’, ‘G’, ‘T’} 가 각각 몇번 이상 등장해야 비밀번호로 사용할 수 있는지 순서대로 주어졌을 때 만들 수 있는 비밀번호의 종류의 수를 구하는 프로그램을 작성하자.
단 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다.

입력:
첫 번째 줄에 민호가 임의로 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다. (1 ≤ |P| ≤ |S| ≤ 1,000,000)
두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.
세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다.
각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.

출력:
만들 수 있는 비밀번호의 종류의 수를 출력해라.
'''

import sys

input = sys.stdin.readline

# 전역 변수 선언
check_list = [0] * 4
my_list = [0] * 4
check_secret = 0


# 함수 선언
def my_add(c):
    global check_list, my_list, check_secret

    if c == 'A':
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            check_secret += 1
    elif c == 'C':
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            check_secret += 1
    elif c == 'G':
        my_list[2] += 1
        if my_list[2] == check_list[2]:
            check_secret += 1
    elif c == 'T':
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            check_secret += 1


def my_remove(c):
    global check_list, my_list, check_secret

    if c == 'A':
        if my_list[0] == check_list[0]:
            check_secret -= 1
        my_list[0] -= 1
    elif c == 'C':
        if my_list[1] == check_list[1]:
            check_secret -= 1
        my_list[1] -= 1
    elif c == 'G':
        if my_list[2] == check_list[2]:
            check_secret -= 1
        my_list[2] -= 1
    elif c == 'T':
        if my_list[3] == check_list[3]:
            check_secret -= 1
        my_list[3] -= 1


# 메인 코드
result = 0
s, p = map(int, input().split())
A = list(input())
check_list = list(map(int, input().split()))

for i in range(4):
    if check_list[i] == 0:
        check_secret += 1

for i in range(p):
    my_add(A[i])
if check_secret == 4:
    result += 1

for i in range(p, s):
    j = i - p
    my_add(A[i])
    my_remove(A[j])
    if check_secret == 4:
        result += 1

print(result)