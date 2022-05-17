from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student
#1. 학생 등록 페이지 stuWrite

def stuWrite(request):
    #어디로 넘길지 확인 함수 
    if request.method == 'GET':
        return render(request,'stuWrite.html')
    else:
        #method가 POST로 올때만.
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')

        #DB저장
        Student.objects.create(s_name=name,s_major=major,s_age=age, s_grade=grade,s_gender=gender)

        #홈페이지 지정한 곳으로 리턴.
        return HttpResponseRedirect(reverse('index'))

#2. 학생 리스트 페이지 stuList
def stuList(request):
    qs = Student.objects.order_by('s_name')
    count = qs.count()
    # dic타입으로 저장
    context = {'stuList':qs,"stuCount":count}
    # context데이터를 html에 보냄
    return render(request,'stuList.html',context)   



#3. 학생 상세 페이지 stuView
def stuView(request,name,major):
    # name변수를 가지고 학생 검색 - 타입 : Student객체
    qs = Student.objects.get(s_name=name)
    context={'stu':qs}
    return render(request,'stuView.html',context)