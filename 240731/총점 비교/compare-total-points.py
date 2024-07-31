class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
mambers = []
for _ in range(n):
    n, k, e, m = tuple(input().split())
    mambers.append(Student(n, int(k), int(e), int(m)))

mambers.sort(key = lambda x: (x.kor + x.eng + x.math))

for Student in mambers:
    print(Student.name, Student.kor, Student.eng, Student.math)