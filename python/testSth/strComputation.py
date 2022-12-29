"""
    문자열 곱하기를 할 경우 곱한 횟수만큼 갯수가 증가하게 된다.
"""

stringTest = "12"
stringTest *= 2
print(stringTest)

"""
    문자형 숫자 정렬 기준
    
"""

strNum = ['01','20','03']
strNum2 = ['1','20','3']
strNum2 = list(map(lambda x: x*3, strNum2))
print(strNum2)
strNum2.append('1')
print(sorted(strNum2,reverse=True))
print(strNum)
