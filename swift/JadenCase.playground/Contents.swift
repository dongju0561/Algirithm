func solution(_ s:String) -> String {
    var result = String()
    var lowerString = s.lowercased()
    var isFirstLettr = true
    
    for c in lowerString{
        if(c != " "){
            if(isFirstLettr){
                result += String(c).uppercased()
                isFirstLettr = !isFirstLettr
            }else{
                result += String(c)
            }
        }else{
            result += String(c)
            isFirstLettr = !isFirstLettr
        }
    }
    
    return result
}

print(solution("hello world"))


