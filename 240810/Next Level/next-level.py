class user:
    def __init__(self, id, level):
        self.id = id
        self.level = level

user1 = user("codetree", 10)

input_id, input_level = input().split()
user2 = user(input_id, int(input_level))

print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")