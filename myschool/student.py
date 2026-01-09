from person import Person
class Student(Person):  # no, name, input_info(), show_info()
    def __init__(self, no=1, name='', cname = None):
        super().__init__(no, name)
        self.cname = cname
    # override
    def input_info(self):
        self.no = input('학번을 입력하세요: ')
        super().input_info()  # 이름 입력
        self.cname = input('학급명을 입력하세요: ')
    def show_info(self):
        info = f'''
        ----------학생 정보----------
        학  번: {self.no}
        학급명: {self.cname}
        {super().show_info()}
        ----------------------------
        '''
        return info