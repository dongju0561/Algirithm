from itertools import combinations, permutations

aList = [1,2,4,3]

# 조합
# aList에 있는 요소로 중복을 허용하지 않고 '두개'의 요소를 갖는 한쌍의 조합을 구해준다.
print(list(combinations(aList,2))) 

# aList에 있는 요소로 중복을 허용하고 '두개'의 요소를 갖는 한쌍의 조합을 구해준다.
print(list(permutations(aList,2))) # 순열

#sum()함수 iterable 변수의 요소들의 전체 합
for pair in combinations(aList,2):
    print(sum(pair))