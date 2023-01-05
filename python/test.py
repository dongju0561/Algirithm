def solution(num):
    answer = 0
    count = 0
    while(num != 1):
        if(num%2 == 0):
            print("work+")
            num /= 2
            print(num)
            count +=1
        elif(num%2 == 1):
            print("work")
            num = num * 3 + 1
            print(num)
            count +=1
            
    answer = count
    return answer

print(solution(6))