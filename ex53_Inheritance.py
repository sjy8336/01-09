# [1] 부모 클래스 : Super클래스 / Base 클래스
class Parent:
    def __init__(self, name='부모', age=0):
        self.name = name
        self.age = age
    def info(self):
        print('Name: %s\nAge: %d세\n'%(self.name, self.age))


# [2] 자식 클래스 : Sub 클래스 / Derived 클래스
# class 클래스명(부모클래스): => 상속관계 "is a" 관계 Student is a Person
class Child(Parent):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)  # 부모클래스(Parent)의 __init__을 호출해서 name과 age를 초기화한다
        # super => 부모로 부터 상속받은 필드나 메서드를 참조할 때 사용하는 키워드
        # self => 자기 자신의 인스턴스 변수나 메서드를 참조할 때 사용하는 키워드
        # self.name = name
        # self.age = age
        self.hobby = hobby
    # 메소드 오버라이딩(overriding) ==> 다형성 특징 중 하나
    # 부모로 부터 상속받은 메소드를 재정의하여 구성하는 것
    def info(self):
        # 이름, 나이, 취미
        # 부모의 info()호출하기
        super().info()
        print('Hobby: %s\n'%(self.hobby), end = '')
        print('-------------------------------')

p1 = Parent()    # 기본생성자
p2 = Parent('김부모')   # 인자 1개 생성자
p3 = Parent('최부모', 55)   # 인자 2개 생성자
p1.info()
p2.info()
p3.info()

# c1 = Child()  #[X]
"""  
TypeError: Child.__init__() missing 3 required positional arguments: 'name', 'age', and 'hobby'
"""
c2 = Child("최영길", 20, "마라톤")
print('-----------------------')
c2.info()