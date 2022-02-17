from django.shortcuts import render
import time
# Create your views here.
def exercise1(request):
    #day=request.GET.get('day','16일')
    #month=request.GET.get('month','2월')
    day1=time.localtime().tm_mday
    month1=time.localtime().tm_mon
    context={'name':'김주영', 'day' :day1, 'month' : month1}
    return render(request,'exercise1.html',context)

def exercise2(request):
    query = 'type' in request.GET
    member=['김주영','강지우','정현석']
    number=3
    if query:
        type=request.GET['type']
        if type=='memberlist':
            result ='우리팀의 팀원을 소개합니다.'
            content={'memberlist':member,'result':result}
        elif type =='number':
            result='우리팀 인원은 3명입니다.'
            content={'result':result, 'num':3}
        else:
            result='type=memberlist 또는 type=number 쿼리를 전달하세요'
            content={'result':result}
    else:
        result = 'type=memberlist 또는 type=number 쿼리를 전달하세요'
        content = {'result': result}
    return render(request,'exercise2.html',content)

def exercise3(request):
    context= {'title':'글 작성하기',}
    if request.method=='POST':
        name=request.POST.get("name","없음")
        memo=request.POST.get("memo","없음")
        context={
            'title':name+'님이 남긴 글입니다.',
            'memo':memo,
            'name':name,
        }
    return render(request,'exercise3.html',context)