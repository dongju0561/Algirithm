#1/2
# y = x기준으로 똑같다는 특징을 이용 한쪽 부분만 비교.. 이것 또한 시간 복잡도...
from itertools import combinations_with_replacement as cwr

def smallThanP(i,j,dMax):
    return dMax >= i ** 2 + j ** 2

def getP(k,d,pList):
    a = 0
    while k*a <= d:
        pList.append(k*a)
        a += 1
    return pList

def solution(k, d):
    answer = 0
    pList = []
    pList = getP(k,d,pList)
    pList = list(cwr(pList,2))
    dMax = d ** 2
    
    for case in pList:
        i,j = case
        if(i == j):
            if smallThanP(i,j,dMax) == True:
                answer += 1
        else:
            if smallThanP(i,j,dMax) == True:
                answer += 2
    
    return answer

print(solution(2,4))

"""
전체 경우의 수를 비교 시간 복잡도 인해 실패...

from itertools import product

def getRangeOfDot(k,d,rangeOfDot):
    a  = 0
    while((a * k) <= d):
        rangeOfDot.append(a * k)
        a += 1
    return rangeOfDot


def solution(k, d):
    answer = 0
    rangeOfDot = []
    cnt = 0
    dlimit = d**2
    rangeOfDot = getRangeOfDot(k, d, rangeOfDot)

    rangeOfDot = list(product(rangeOfDot,repeat = 2))
    print(rangeOfDot)
    for case in rangeOfDot:
        i,j = case
        
        if(i > d or j > d or (i == d and j != 0) or (j == d and i != 0)):
            continue
        if(dlimit >= i**2 + j**2):
            cnt += 1

    return cnt
"""