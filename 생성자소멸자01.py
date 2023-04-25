# -*- 생성자와 소멸자 -*-
class MyClass:
    #가장 먼저 실행되는 초기화 메서드(생성자) 
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #가장 마지막에 인스턴스를 소멸하면서 실행되는 메서드(소멸자) 
    def __del__(self):
        print("Instance is deleted!")

m = MyClass(5)
#del m 

print("전체 코드 실행 종료")