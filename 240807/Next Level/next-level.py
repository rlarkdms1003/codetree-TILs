class User:
    def __init__(self, user_id, level):
        self.user_id = user_id
        self.level = level

user1 = User("codetree", 10)


input_id, input_level = input().split()
user2 = User(input_id, int(input_level))


print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")