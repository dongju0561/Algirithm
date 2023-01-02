"""
    
"""

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command # command의 list 요소들을 차례대로 변수에 할당할 수 있다.
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer