"""  
Person 클래스
- no, name
- input_info()
- show_info() 구성하세요

Student 클래스에서
Person을 상속받고
- cname 추가하세요
- show_info() 오버라이딩 하세요
"""
# 내가 함
""" 
class Person:
    def __init__(self, no, name):
        self.no = no
        self.name = name
    def input_info(self):
        print('------------')
        print(input('입력하세요 >>'))
    def show_info(self):
        print(f'''  
        학  번: {self.no}
        이  름: {self.name}
        ''')

class Student(Person):
    def __init__(self, no, name, cname):
        super.__init__(no, name)
        self.cname = cname
    def show_info(self):
        super.show_info()
        print(f'학급명: {self.cname}')
"""

class Person:
    def __init__(self, no=1, name='아무개'):
        self.no = no
        self.name = name
    def show_info(self):
        return f"""이름: {self.name}"""
    def input_info(self):
        self.name = input('이름을 입력하세요: ')