import collections

def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine) # 딕셔너리 형식으로 각각의 숫자의 갯수를 key값은 숫자의 종류, value는 해당 숫자의 갯수로 생성해준다.

    for v in sorted(cnt.values(), reverse = True): #cnt.values()는 cnt 딕셔너리의 value값을 추출하고 sorted(,reverse = True) 함수를 통해 내림차순 순으로 정렬한다.
        k -= v #반복이 진행하면서 k값을 줄이고
        answer += 1 #타입이 바뀔때마다 사용한 사이즈 타입의 갯수를 증가 시킨다.
        if k <= 0: # k값이 0보다 작게 된다면 판매하기 충분한 양을 처리할 수 있기 때문에 
            break # break한다.
    return answer

solution(3,{1,3,2,1})