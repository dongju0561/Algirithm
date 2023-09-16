/*
 최대값 최소값
 https://school.programmers.co.kr/learn/courses/30/lessons/12939
 */
func solution(_ s:String) -> String {
    var isFirstTime = true
    var numMax = Int()
    var numMin = Int()
    var num = Int()
    var string = String()
    for numChar in s{
        if(" " != numChar){
            string.append(String(numChar))
            
        }else{
            num = Int(string)!
            if(isFirstTime){
                numMax = num
                numMin = num
                isFirstTime = false
            }
            string = ""
            if(numMax < num){ numMax = num }
            if(numMin > num){ numMin = num }
        }
        
    }
    num = Int(string)!
    if(numMax < num){ numMax = num }
    if(numMin > num){ numMin = num }
    return "\(numMin) \(numMax)"
}
