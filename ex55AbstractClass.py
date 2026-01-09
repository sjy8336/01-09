"""  
추상클래스를 만들어서 메소드 이름을 다르게 짓는 것을 막아보자
- 추상클래스를 상속받은 자식 클래스에서는 반드시 추상메소드를 오버라이드 해야 한다. 
    이름을 다르게 구성하면 오류 발생함
- 추상클래스는 abc모듈의 ABC클래스를 상속받아서 만든다
- 추상클래스는 1개 이상의 추상메소드를 갖는다 
    @abstractmethod라는 장식자를 붙여 추상메소드를 구성한다
"""
# Flyer : 비행체 fly() 메소드
# Bird / AirPlane / PaperAirPlane
from abc import ABC, abstractmethod    # Abstract Base Class 약자
class Flyer(ABC):   # 추상클래스
    @abstractmethod
    def fly(self):
        pass
# 추상클래스를 상속받은 자식 쪽에선 반드시 추상메소드를 동일한 이름으로 재정의해야 함
class Bird(Flyer):
    def fly(self):  # 오버라이드
        print('새가 훨훨 날아요~~~')

class AirPlane(Flyer):
    def fly(self):
        print('비행기가 휙휙 날아요~~~')

class PaperAirPlane(Flyer):
    # pass
    # def flying(self):
    def fly(self):  # 반드시 오버라이드 해야 함. 안하면 자신도 추상클래스가 된다
        print('종이비행기가 사뿐히 날아요~~~')

# TypeError: Can't instantiate abstract class PaperAirPlane without an implementation for abstract method 'fly'

# 부모가 같은 객체들은 같은 자료형으로 간주된다
# f1 = Flyer()    # 추상클래스는 객체화시킬 수 없다
f2 = Bird()
f3 = AirPlane()
f4 = PaperAirPlane()
arr = [f2, f3, f4]
# for 루프 돌면서 arr에 저장된 객체들의 fly() 메소드 호출해보기
for i in arr:
    i.fly()
    print('----------------------------------')