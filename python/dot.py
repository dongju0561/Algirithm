#1/2
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

print(solution(1000,10000))