"""
    주어진 정수 리스트를 가지고 만들 수 있는 가장 큰 수를 만들어라
    예를 들어 정수 리스트로 numbers = [1,23,2,4]
    입력값으로 만들 수 있는 가장 큰 정수는 42321이다.
    그리고 가장 큰 정수값을 만들고 문자열 형식으로 반환하여라
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: x*3, reverse=True) 
    # sort(key=)는 key 파라미터안에 람다를 각 요소마다 적용시키고 정렬을 시킨다.
    # 그 후에 다시 원래의 값으로 돌려 놓는다.
    return str(int(''.joint(numbers)))

"""
    문제를 풀고 알게된 내용
    map()함수의 개념, lambda의 개념, sort(key=)를 통한 정렬
"""