class Student: #main이 있는 파일 하위에 package화 된 class
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg = 0
    rank = 0

    def __init__(self,stuname='',kor=0,eng=0,math=0):
        Student.stuno += 1 #단 하나, 클래스 변수
        self.stuno = Student.stuno #1씩 자동으로 올라갈 학번.
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total =kor + eng + math
        self.avg = self.total/3
        self.rank = 0


    def __str__(self): #문자열로 반환해줌.
        stuprint = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,\
            self.stuname,self.kor,self.eng,self.math,self.total,self.avg,self.rank)
        return stuprint

    def __eq__(self,stuname): #메소드(객체)가 같은지 비교
        return self.stuname == stuname

    def __lt__(self,other): #내부 total과 외부의 total을 비교 외부 total이 큰가?
        return self.total < other.total

    def getKor(self): #kor에 대한 외부 접근 차단.
        return self.__kor

    def setKor(self,kor): #kor에 입력되는 값이 음수일 경우 원래 kor값으로 입력
        if kor>=0:
            self.kor=kor
            self.total =kor + self.eng + self.math
            self.avg = self.total/3
            
        else:
            print('입력이 잘못되었습니다')

    def getEng(self): #eng에 대한 외부 접근 차단.
        return self.__eng

    def setEng(self,eng): #eng에 입력되는 값이 음수일 경우 원래 eng값이로 입력
        if eng>=0:
            self.eng = eng
            self.total = self.kor + eng + self.math
            self.avg = self.total/3
        else:
            print('입력이 잘못되었습니다.')

    def getMath(self): #math에 대한 외부 접근 차단.
        return self.__math

    def setMath(self,math): #math에 입력되는 값이 음수일 경우 원래 math값으로 입력
        if math>=0:
            self.math = math
            self.total = self.kor + self.eng + math
            self.avg = self.total/3
        else:
            print('입력이 잘못되었습니다.')