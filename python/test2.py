from collections import Counter
def perFault(stages,numStage,N):
    
    current = stages.get(numStage)
    passed = 0
    for man in stages:
        passed = passed + stages.get(man)
    return current/passed
    

def solution(N, stages):
    Fdic = {}
    stages = dict(Counter(stages))
    for stage in range(1,N):
        Fdic[stage] = perFault(stages,stage,N)
    #딕셔너리 값을 기준으로 키값 정렬
    answer = []
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])