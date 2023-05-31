from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Comment, Dashboard
from django.core.paginator import Paginator
from .forms import TaskForm

# Create your views here.

def user_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            dashboard = Dashboard.objects.get(user=user)
        except Dashboard.DoesNotExist:
            dashboard = Dashboard.objects.create(user=user)
        
        #tasks = dashboard.tasks.all()
        tasks = Task.objects.filter(created_by =user, archived=False).order_by('-created_at')

        paginator = Paginator(tasks, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        context = {
            'dashboard': dashboard,
            'tasks': page_obj
        }
        return render(request, 'task_manager/user_dashboard.html', context)
    else:
        return redirect('users:login')

def create_task(request):

    form = TaskForm(request.POST or None)
    if form.is_valid():
        task =form.save(commit=False)
        task.created_by = request.user
        task.save()

        dashboard, _ = Dashboard.objects.get_or_create(user=request.user)
        dashboard.tasks.add(task)

        return redirect('user_dashboard')
    
    context = {
    'form' : form
    }
        
    return render(request, 'task_manager/create_task.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    dashboard = Dashboard.objects.get(user=request.user)
    if request.method == 'POST':
        dashboard.tasks.remove(task)
        task.delete()
        return redirect('user_dashboard')
    context ={
        'dashboard': dashboard,
        'task': task
    }
    return render(request, 'task_manager/delete_task.html',context)

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
   
    if request.method == 'POST':
        form =TaskForm(request.POST, instance = task)
        if form.is_valid():
            updated_task = form.save()

            dashboard, _ = Dashboard.objects.get_or_create(user=request.user)
            dashboard.tasks.add(updated_task)

            return redirect('user_dashboard')
        

    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task
    }

    return render(request, 'task_manager/update_task.html', context)

def add_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        content = request.POST['content']
        created_by = request.user
        comment = Comment.objects.create(task=task, content=content, created_by=created_by)
        return redirect('user_dashboard')
    
    context = {
        #'comment':comment,
        'task':task
    }
    return render(request, 'task_manager/add_comment.html', context)

def archive_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        archived = request.POST.get('archived', True)
        task.archived = archived
        task.save()
        return redirect('user_dashboard')
    return render(request, 'task_manager/archive_task.html', {'task': task})

def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()
    
    context = {
        'task': task,
        'comments': comments
    }
    
    return render(request, 'task_manager/view_task.html', context)

def view_task_archives(request):
    user = request.user
    archived_tasks = Task.objects.filter(created_by=user, archived=True)
    
    context = {
        'archived_tasks': archived_tasks
    }
    
    return render(request, 'task_manager/task_archives.html', context)
