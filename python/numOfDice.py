"""
    주사위 갯수
    정육면체 상자 안에 모서리 길이가 n개인 주사위를 몇개난 넣을 수 있을지
    상자의 길이는 box 리스트에 저장된단 box[0]:가로 box[1]:세로 box[2]:높이
    몇개나 넣을 수 있을까?
"""
def solution(box, n):
    solution = 1
    for length in box: # 각각 주사위가 들어올 수 있는 갯수를 계산
        solution *= length // n 
        # length에 들어갈 수 있는 n길이의 주사위가 들어갈 수 있는 최대 갯수 구하기 위해 몫을 구함
    return solution