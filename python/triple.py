"""
    itertool 패키지를 통해 순열 조합을 구할 수 있다.
    해당 문제에서는 순서는 중요하지 않고 3개의 한쌍을 구하는 문제이니 전체 조합을 구하고 조합쌍의 합이 0이 되는 것을 찾아
    cnt를 늘려 cnt값을 반환하게 하면된다.

    combinations(iterable, int): 배열에 요소들로 int개 한쌍으로 구할 수 있는 전체 갯수를 구한다.
    하나씩 조회하여 한쌍의 합을 sum()함수를 이용하여 구하고 연산값이 0이 된다면 cnt을 증가 시켜 cnt값을 반환한다.
"""
from itertools import combinations

def solution(numbers):
    cnt = 0
    for i in combinations(numbers,3):
        if sum(i) == 0:
            cnt += 1
    return cnt

print(solution([-2, 3, 0, 2, -5]))