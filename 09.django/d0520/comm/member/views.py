from django.http import HttpResponse
from django.shortcuts import redirect, render
from member.models import Member


def login(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    else:

        id = request.POST.get('id')
        pw = request.POST.get('pw')

        try:
            qs = Member.objects.get(id=id, pw=pw)
            request.session['session_id'] = qs.id
            request.session['session_name'] = qs.name
            request.session['session_nickname'] = qs.nickname
            return redirect ('/')
        except Member.DoesNotExist:
            qs = None
            context={'msg':'아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인 바랍니다.'}
            return render(request,'login.html',context)

# logout페이지 함수
def logout(request):
    request.session.clear()
    return redirect('/')


def list(request):
    qs = Member.objects.order_by('id')
    context = {'memberList':qs}
    return render (request,'list.html',context)