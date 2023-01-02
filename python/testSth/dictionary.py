import collections

list = [1,3,2,2,1,4]

#collections 모듈에서 Counter를 사용하여 중복되는 요소의 갯수를 구하는 함수
cnt = collections.Counter(list)
print(cnt)

for i in sorted(cnt.values(),reverse=True):
    print(i)
