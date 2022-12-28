#map함수 연습
"""
    원의 반지름값이 list형식으로 주워졌을때 map함수를 통해 각가의 원의 넓이를 구하는 map함수를 만듬
"""
# map 첫번째 argument로 function을 사용한 케이스
def widthOfCircle(radius): 
    return radius*radius*3.14

radiusList = [2,4,1,5]

print(list(map(widthOfCircle, radiusList)))

# map 첫번째 argument로 lambda를 사용한 케이스
listInput = ["hello", "world","Korea"]
listCase = list(map(lambda x:  len(x), listInput))
tupleCase = tuple(map(lambda x:  len(x), listInput))
print(listCase)
print(tupleCase)

