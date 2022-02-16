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