/*
 프로그래머스 달리기 경주
 https://school.programmers.co.kr/learn/courses/30/lessons/178871
 */

import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var player = players
    var call = callings
    var rank = [String : Int]()
    
    for i in 0 ..< player.count{
        rank[player[i]] = i
    }
    
    for i in 0 ..< call.count{
        var idx = rank[call[i]]!
        var temp = player[idx - 1]
        player[idx - 1] = player[idx]
        player[idx] = temp
        rank[call[i]]! -= 1
        rank[temp]! += 1
    }
    
    return player
}
