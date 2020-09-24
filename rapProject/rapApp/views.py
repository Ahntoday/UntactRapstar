from django.shortcuts import render, redirect
from .models import Beat

# Create your views here.
def home(request):
    context = {"beat": Beat.objects.all()[0]}

    return render(request, "home.html", context)

def choice(request):
    ## nickname 있으면 session에다가 저장
    if record:
        context = {}
        ## User db에 없는 nickname이면 되돌아가기
        ## User db에 이미 녹음본이 있으면 redirect(result)
        ## DB에서 비트, 가사 가져오기
        return render()
    if vote:
        context = {}
        ## User DB 가져올 것
        return render()
    if result:
        return redirect(result)

def result(request):
    ## DB에서 vote table 참가자마다 count
    ## count 가장 높은 참가자가 우승자
    return render()

def saveRecord(request):
    ## User DB update
    print(request.POST)
    return render()