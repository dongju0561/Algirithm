func solution(_ targets:[[Int]]) -> Int {
    var ans = 0
    let sorted = targets.sorted(by: { $0[1] < $1[1] })    
    
    var end = sorted[0][1]

    for target in sorted { 
        if target[0] >= end {
            end = target[1]
            ans += 1
        }
    }
    return ans + 1
}

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))

