def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command # 각 요소들을 미리 i,j,k 변수에 옴겨두고
        answer.append(list(sorted(array[i-1:j]))[k-1]) 
        # array를 i,j변수를 가지고 slicing을 진행하고 k-1번째에 있는 값을 answer리스트에 append한다.
    return answer

"""
    map함수를 이용하여 commands의 각각의 요소들에 접근 요소안의 i,j,k값을 이용하여 원하는 값을 추출하고 추출한 값들을
    list화 한다.
"""
def another_solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))