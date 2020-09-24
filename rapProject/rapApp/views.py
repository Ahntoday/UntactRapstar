from django.shortcuts import render, redirect
from .models import Beat, User, Vote, Lyrics
from django.core.files.storage import FileSystemStorage
import datetime


# Create your views here.
def home(request):

    return render(request, "home.html")

def choice(request):
    ## nickname 있으면 session에다가 저장
    if request.POST:
        if "nickname" in request.POST:
            request.session["nickname"] = request.POST["nickname"]
        context = {}
        if "rapper_btn" in request.POST:
            ## User db에 없는 nickname이면 되돌아가기
            # user = User.objects.filter(nickname=request.POST["nickname"])
            # if len(user) == 0:
            #     return redirect(home)
            # ## User db에 이미 녹음본이 있으면 redirect(wait)
            # print(user[0].rap)
            ## DB에서 비트, 가사 가져오기
            context["beats"] = Beat.objects.order_by("?").all()[:5]

            context["lyrics"] = Lyrics.objects.order_by("?").all()[:5]
            return render(request, "record.html", context)
        if "audience_btn" in request.POST:
            user = Vote.objects.filter(user=request.POST["nickname"])
            print(user)
            if len(user) != 0:
                return redirect(wait)
            ## User DB 가져올 것
            context["rappers"] = User.objects.all()
            return render(request, "vote.html", context)
    return redirect(home)

def wait(request):
    # 여기서 뽑은 애 DB에 저장
    if request.POST:
        print(request.POST)
        if("rapstar" in request.POST):
            vote = User.objects.get(pk=request.POST["rapstar"][0])
            Vote.objects.create(
                user = request.session["nickname"],
                vote = vote
            )
    return render(request, "result_wait.html")

def result(request):
    ## DB에서 vote table 참가자마다 count
    ## count 가장 높은 참가자가 우승자

    context = {}
    winner = ""
    max_count = 0
    rappers = User.objects.all()
    for rap in rappers:
        count = len(Vote.objects.filter(vote=rap))
        if max_count <= count:
            max_count = count
            winner = rap.nickname
    context["winner"] = winner
    context["count"] = max_count
    return render(request, "result.html", context)

def saveRecord(request):
    ## User DB update
    if request.POST:
        myfile = request.FILES['fileToUpload']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        User.objects.filter(nickname=request.session["nickname"]).update(rap=filename)
    return redirect(wait)