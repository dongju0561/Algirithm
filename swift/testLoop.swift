/*
이진 변환 반복하기

내가 사용한 메소드

String(_ number:Int, radix: Int)
radix값에 따라서 10진수에서 x진수값으로 변환 해준다.

*/
import Foundation

func convert(_ s:String, _ listZero:inout [Int]){
    var numOfZero = Int()
    var numOfOne = Int()
    
    if(s == "1"){return}

    for c in s{
        if(c == "0"){numOfZero += 1} //0의 갯수
        else{numOfOne += 1} //1의 갯수
    }
    listZero[0] += 1
    listZero[1] += numOfZero
    
    if(numOfOne != 1){
        return convert(String(numOfOne,radix: 2), &listZero)
    }
}

func solution(_ s:String) -> [Int] {
    var result = [0,0]
    
    convert(s, &result)
    return result
}

print(solution("110010101001"))
