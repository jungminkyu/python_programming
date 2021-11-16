"""
파이썬 모듈 안에는 함수와 클래스를 선언할 수 있다.
"""

def add(n1, n2) :
    #pass
    return n1+n2

print(add(10,20))
print(type(add))

# 실행 : Ctrl + shift + f10

add2 = lambda n1, n2 : n1 + n2
#함수명, 문법 등이 사라지고, 인수와 body만 남은 함수
print(add2(100, 200))
print(type(add2))

#class 선언
class User() :
    #생성자 선언
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

#객체 생성
user = User("파이썬")
print(user)