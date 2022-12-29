def solution(numbers):
    numbers = list(map(str, numbers)) # number 문자열로 전환
    numbers.sort(key=lambda x: x * 3, reverse=True) 
    # [1,21,2,4]리스트가 들어왔을때 key에 들어온 함수를 수행 후 내림차순으로 정렬을 하게 된다.
    # 우선 문자열 리스트에서 정렬 기준은 영어, 한국어(가나다순), 숫자 순으로 정렬이된다.

    print(numbers[1])
    return str(int(''.join(numbers)))

solution([1,21,2,4])