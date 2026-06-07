from django.shortcuts import render,redirect
from User.models import CyberTweets
# Create your views here.
def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST['username']
            pswd = request.POST['password']
            if usid == 'admin' and pswd == 'admin':
                return redirect('adminhome')

    return render(request,'adminlogin.html')

def adminhome(request):
    cyber=CyberTweets.objects.all()
    return render(request,"adminhome.html",{"cyber":cyber})