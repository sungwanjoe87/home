words = {
    '자동차':'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '직업':'job',
    '사과':'apple',
    '사자':'lion',
    '여우':'fox'    
}
words2 = {
    '연필': 'pencil',
    '자': 'ruler',
    '책': 'book',
    '양말':'socks',
    '모자':'hat',
    '개':'dog',
    '잠':'sleep',
    '먹다':'eat',
    '읽다':'read',
    '피아노':'piano'
}
print('[ 영단어 테스트 ]')
print('1. 초등 1~2학년')
print('2. 초등 3~4학년')
print('0. 프로그램을 종료합니다')

ch1 = int(input('난이도를 선택하시거나, 0번을 눌러 종료하시기 바랍니다.'))

#난이도 선택

if ch1 ==1:
    level=words
elif ch1 ==2:
    level=words2
elif ch1 ==0:
    exit()
wordlist =[] #내가 답변한 정답 오답이 모두 저장되는 리스트.

for word in level:
    inwds = input('{}의 영단어를 입력하세요.'.format(word))
    if inwds.isdigit():
        if inwds == 0:
            print('프로그램을 종료합니다.')
            break
    if level[word] == inwds:
        #정답 ->정답입니다. 자동차:car
        print('정답입니다. {} : {}'.format(word,level[word]))
        #정답 n항목 : car, O, 자동차, car #1차 리스트 형태로
        wlist = [inwds, 'O', word, level[word]]
        #저장 wordlist [[car, O, 자동차, car], [......]]
        wordlist.append(wlist)

    else:
        #오답 -> 오답입니다. 자동차:car
        print('오답입니다. {} : {}'.format(word,level[word]))
        #오답 n합목 : crr, X, 자동차, car #1차 리스트 형태로
        wlist = [inwds, 'X', word, level[word]]
        #저장 wordlist [[car, X, 자동차, car], [......]]
        wordlist.append(wlist)

#정답, 오답 카운트 변수 선언

ocount, xcount = 0,0

#정답, 오답 출력
print('[ 정답확인 ]')
print('='*50)


for idx,wlist in enumerate(wordlist): #정답, 오답이 모두 저장된 2차원 리스트
    if 'O' in wlist: #wordlist안의 1차원 리스트 wlist에 O가 있는지 확인.
        ocount +=1
        print('{}.{}. {}:{}'.format(idx+1,'정답',wlist[2],wlist[3],wlist[0]))
    else:
        xcount +=1
        print('{}.{}. {}:{},    내가 적은 답:{}'.format(idx+1,'오답',wlist[2], wlist[3],wlist[0]))

#최종 정답 오답 갯수 및 점수 출력.
print('='*50)

print('정답: {}개, 오답: {}개, 총 {}점'.format(ocount,xcount,ocount*10))