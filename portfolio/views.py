from django.shortcuts import render
from . models import Project
from .forms import NewMessages



# Create your views here.
def indexpage(request):
    
    form = NewMessages
    projects = Project.objects.all()
    if(request.method =='POST'):
        form = NewMessages(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return(render(request,'portfolio/new.html',{'projects':projects,'form':form}))
    return(render(request,'portfolio/home.html',{'projects':projects,'form':form}))
    



    
