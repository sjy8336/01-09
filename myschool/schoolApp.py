from person import Person
from student import Student
from teacher import Teacher

class SchoolApp:
    def __init__(self):
        self.arr = []  # 빈 리스트
        self.count = 0  # 등록 인원 수

    def main_menu(self):
        print('---------Menu-----------')
        print(' 1. 등  록')
        print(' 2. 출  력')
        print(' 3. 검  색')
        print(' 4. 삭  제')
        print(' 9. 종  료')
        print('------------------------')
    def sub_menu(self):
        print('--- Sub Menu-----------')
        print(' 1. 학  생')
        print(' 2. 교  사')
        print(' 3. 직  원')
        print(' 4. 상위 메뉴')
        print('------------------------')
    # 1. 등록
    def join(self):
        while True:
            self.sub_menu()
            num = int(input('메뉴 번호를 선택하세요: '))
            if num not in (1, 2, 3, 4):
                print('>>메뉴에 없는 번호입니다. 다시 입력하세요<<')
                continue
            if num == 4:   # 상위 메뉴
                return   # join()을 호출한 쪽으로 돌아감
            elif num == 1:
                p = Student()
            elif num == 2:
                p = Teacher
            elif num == 3:  # 직원 객체 생성
                pass
            p.input_info()  # 입력받는 작업
            print(p.show_info())
            yn = int(input('위 정보를 등록할까요? 1. yes 2. No'))
            if yn == 1:
                self.arr.append(p)
                self.count += 1
                print(f'>>등록 완료!! 현재 등록된 인워 : {self.count}명<<')
            else:
                print('>>등록을 취소했습니다<<')
    # 2. 전체 출력
    def print_all(self):
        if self.count <= 0:
            print('>>등록된 정보가 없습니다')
            return
        for p in self.arr:
            print(p.show_info())
    # 3. 검색
    def find(self):
        name = input('검색할 사람의 이름을 입력하세요: ')
        is_exist = False
        for p in self.arr:
            if p.name == name:
                is_exist = True
                print(p.show_info())  # 검색한 사람 정보 출력
        if not is_exist:
            print(f'>>{name}님은 존재하지 않습니다<<')
    # 4. 삭제
    def delete(self):
        try:
            no = int(input('삭제할 사람의 번호(학번/교번/사번)를 입력하세요: '))
            for p in self.arr:
                if p.no == str(no):
                    self.arr.remove(p)
                    print(f'>>{no}번 {p.name}님 정보를 삭제했습니다<<')
                    return
            print(f'>>{no}번 회원은 존재하지 않습니다<<')
        except Exception as ex:
            print(f'>>입력오류!! 번호를 입력해야 해요<<')
            return
    # process 프로그램 흐름 제어 메서드

    def process(self):
        while True:
            self.main_menu()
            num = int(input('메뉴 번호를 선택하세요'))
            if num == 9:
                print('Bye Bye~~')
                exit(0)
            # 유효성 체크
            if num not in (1, 2, 3, 4):
                print('>>메뉴에 없는 번호입니다. 다시 입력하세요.<<')
                continue
            if num == 1:
                self.join()
            elif num == 2:
                self.print_all()
            elif num == 3:
                self.find()
            elif num == 4:
                self.delete()

if __name__ == '__main__':
    p1 = Person(1, '송영길')
    s1 = Student(100, '홍길동', '파이썬반')
    # p1.input_info()
    # print(p1.show_info())
    print('--------------------------')
    # s1.input_info()
    # print(s1.show_info())
    t1 = Teacher(200, '신승호', 'JavaScript')
    t1.input_info()
    print(t1.show_info())