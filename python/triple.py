from collections import Counter
#함수 음수 갯수 세기

def cntNegative(numbers):
    cnt = 0
    for num in numbers:
        if(num < 0):
            cnt += 1
        else: 
            break
    return cnt

def solution(numbers):
    answer = 0
    numbers.sort()
    Neg = cntNegative(numbers)
    negNums = numbers[0:Neg]
    numbers = numbers[Neg:]
    cntNum = dict(Counter(numbers))

    for neg in negNums:
        for pos in numbers:
            temp = neg + pos
            if temp < 0:
                if temp == pos:
                    print("")
            elif temp == 0:
                if cntNum[0] >= 1:
                    answer += 1


    return answer

print(solution([1,2,-1,-2,3,0,0]))

"""
셋이 0일때, 하나가 0이고 두개의 수의 합이 0이 될때(-1을 곱했을때 같을 수),

-4 = 0,1,2,3,4

"""
