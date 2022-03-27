class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuname='',kor=0,eng=0):
        Student.stuno += 1 #유일 클래스 변수 선언.
        self.stuno = Student.stuno # 자동으로 번호 올라가게 함.
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor+eng
        self.avg = self.total/2
        self.rank =0
    def __str__(self): #문자열 자동 출력 함수
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,\
            self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint

# 같은지 비교
    def __eq__(self,stuname):
        return self.stuname == stuname
#객체(근데 오브젝트? 메소드? 인스턴스? 영어 번역이라 헷갈림.)
    def __lt__(self,other):
        return self.total < other.total

    def getKor(self): #kor에 대한 외부 접근 차단시 사용
        return self.__kor

    def setKor(self,kor):
        if kor>=0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

    def setEng(self,eng): #eng에 대한 외부접근 차단 함수
        if eng>=0:
            self.eng=eng
            self.total=self.kor+eng
            self.avg = self.total/2
        else:
            print('입력이 잘못되었습니다.')

