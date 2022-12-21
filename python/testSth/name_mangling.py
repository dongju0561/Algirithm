"""
클래스 내부의 메소드의 파라미터 self의 의미

여기서 self는 클래스 자기 자신(id)을 의미한다.
일반 함수는 정의할때 self라는 파라미터를 생성하지 않지만 클래스 내부에 위치한 메소드들은 항상 파라미터 self를 가져야한다. 
그렇지 않을 경우 콘솔창에는 파라미터가 부족하다고 뜨게 될것이다.
"""

class Class1:    
    def print_Class1_id(self):
        print(id(self))


class Class2(Human):
    def print_Class2_id(self):
        print(id(self))

class1 = Class1()
class2 = Class2()

class1.print_Class1_id()
class2.print_Class2_id()
