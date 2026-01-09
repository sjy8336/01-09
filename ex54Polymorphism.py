"""  
다형성 (Polymorphism)
- 여러 가지 형태를 가질 수 있는 특성
- 같은 모양의 코드가 다른 동작을 하는 것 (메소드 오버라이딩도 다형성의 한 예)
"""
# Flyer : 비행체 fly() 메소드
# Bird / AirPlane / PaperAirPlane
class Flyer:
    def fly(self):
        print('fly()원형 메소드: 날다~~~')

class Bird(Flyer):
    def fly(self):  # 오버라이드
        print('새가 훨훨 날아요~~~')

class AirPlane(Flyer):
    def fly(self):
        print('비행기가 휙휙 날아요~~~')

class PaperAirPlane(Flyer):
    # pass
    def flying(self):
        print('종이비행기가 사뿐히 날아요~~~')

# 부모가 같은 객체들은 같은 자료형으로 간주된다
f1 = Flyer()
f2 = Bird()
f3 = AirPlane()
f4 = PaperAirPlane()
arr = [f1, f2, f3, f4]
# for 루프 돌면서 arr에 저장된 객체들의 fly() 메소드 호출해보기
for i in arr:
    i.fly()
    print('----------------------------------')