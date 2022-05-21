from django.shortcuts import redirect, render
from member.models import Member


#전체 회원 리스트 함수.

def list(request):
    qs = Member.objects.order_by('-m_no')
    context = {'memberList':qs}
    return render (request,'list.html',context)


#로그인 페이지 함수.

def login(request):
    if request.method =='GET':
        return render(request,'login.html')

    else:
        id = request.POST.get('m_id')
        pw = request.POST.get('m_pw')

        try:
            qs = Member.objects.get(m_id=id, m_pw=pw)
        except Member.DoesNotExist:
            qs = None
        

        #qs가 존재하면.

        if qs:
            request.session['session_id']=qs.m_id
            request.session['session_name']=qs.m_name
            request.session['msg'] = '정상적으로 로그인 되었습니다.'

            #메인페이지로 리턴.
            return redirect('/')
        else:
            msg = '아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인 하세요.'
            return render(request,'login.html',{'message':msg})
            


# 로그아웃 함수
def logout(request):

    request.session.clear()
    return redirect('/')