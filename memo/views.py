from django.shortcuts import render,redirect
from .models import Day
from .forms import DayForm
import datetime
#git new branch
# master i
def day(request,pk):
    now = datetime.datetime.now()# current date and time

    date_time = now.strftime("%d/%m/%Y")

    day1=Day.objects.get(id=pk)
    form = DayForm(instance=day1)
    if request.method=='POST':
        form=DayForm(request.POST,instance=day1)
        if form.is_valid():
            form.save()
            
    context={'form':form,'day':day1,'date':date_time }
    return render(request,'memo/index.html',context)



def home(request):
    x = datetime.datetime.now()
    mnt=x.day
    return redirect('/day/'+str(mnt))
