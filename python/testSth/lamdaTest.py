"""
람다는 함수명을 가지지 않는 함수라고 할 수 있다.
: 이전의 값은 argument를 의미하고 : 이후에 오는 것은 표현식이다.
(lambda argument : 표현식)(입력값)
"""

inputInt = int(input()) # input은 문자열 형태로 반환하게 된다.

print((lambda x: x + 1)(inputInt))
