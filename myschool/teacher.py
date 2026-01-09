from person import Person

class Teacher(Person):
    def __init__(self, no=1, name='', subject = None):
        super().__init__(no, name)
        self.subject = subject
    def input_info(self):
        self.no = input('교번을 입력하세요: ')
        super().input_info()  # 이름 입력
        self.subject = input('교과목을 입력하세요: ')
    def show_info(self):
        info = f'''
        ----------교사 정보----------
        교  번: {self.no}
        교과명: {self.subject}
        {super().show_info()}
        ----------------------------
        '''
        return info