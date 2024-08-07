class BombDefuse:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

# 입력 받기
code, color, second = input().split()

# 객체 생성
bomb_defuse = BombDefuse(code, color, int(second))

# 결과 출력
print(f"code : {bomb_defuse.code}")
print(f"color : {bomb_defuse.color}")
print(f"second : {bomb_defuse.second}")