from django.shortcuts import render,redirect
from .models import Video
from .forms import Videoform
# Create your views here.

def index(request):
    videos = Video.objects.order_by('-date_added')
    context = {'videos':videos}
    return render(request, 'videorequest/index.html', context)

def vrform(request):
    if request.method =='POST':

        form = Videoform(request.POST)

        if form.is_valid():
            new_req = Video(videotitle = request.POST['videoname'], videodesc = request.POST['videodesc'])
            new_req.save()
            return redirect('index')
            # return httpResponseRedirect('/thanks')
    else:
        form = Videoform()

    context = {'form':form}
    return render(request,'videorequest/vrform.html', context)
