from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    #print(request.POST)
    # print(request.POST["task"])
    task=request.POST["task"]
    Task.objects.create(task=task)
    #return HttpResponse('The form is submitted')
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    # return HttpResponse(pk)
    task.is_completed=True
    task.save()
    return redirect('home')
    # return HttpResponse(task)

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')
    # return HttpResponse(task)

def editTask(request,pk):
    get_task =get_object_or_404(Task,pk=pk)
    # print(get_task)
    if request.method == "POST":
        new_task =request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)

def deleteTask(request,pk):
    task =get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
