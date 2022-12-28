def solution(numbers):
    numbers = list(map(str, numbers)) # number 문자열로 전환
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers[1])
    return str(int(''.join(numbers)))

solution([1,21,2,4])