from django.shortcuts import render, redirect
from django.contrib import messages
from admin_app.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/auth/admin/login/')
def dashboard(request):
    current_page = 'dashboard'
    total_projects = Project.objects.count()
    total_completed_projects = Project.objects.filter(status=True).count()
    total_ongoing_projects = Project.objects.filter(status=False).count()
    total_messages = Message.objects.count()

    context = {
        'current_page': current_page,
        'total_projects': total_projects,
        'total_completed_projects': total_completed_projects,
        'total_ongoing_projects': total_ongoing_projects,
        'total_messages': total_messages,
    }
    return render(request, 'admin_app/pages/dashboard.html', context)


@login_required(login_url='/auth/admin/login/')
def project_list(request):
    current_page = 'project_list'
    projects = Project.objects.all()
    context = {
        'current_page': current_page,
        'projects': projects
        }
    return render(request, 'admin_app/pages/project_list.html', context)

@login_required(login_url='/auth/admin/login/')
def project_view(request, project_id):
    current_page = 'project_view'
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project_list')
    context = {
        'current_page': current_page,
        'project':project
    }
    return render(request, 'admin_app/pages/project_view.html', context)

@login_required(login_url='/auth/admin/login/')
def project_add(request):
    current_page = 'project_add'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        head = request.POST.get('head')
        description = request.POST.get('description')
        status = request.POST.get('status') == 'on'
        try:
            project = Project(
                image=image,
                head=head,
                description=description,
                status=status,
            )
            project.save()
            messages.success(request, 'Project added successfully')
            return redirect('project_list')
        except Exception as e:
            messages.error(request, f'Error adding project: {e}')
            return redirect('project_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin_app/pages/project_add.html', context)

@login_required(login_url='/auth/admin/login/')
def project_edit(request, project_id):
    current_page = 'project_edit'
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project_list')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            project.head = request.POST.get('head')
            project.description = request.POST.get('description')
            project.status = request.POST.get('status') == 'on'

            # Update the image field
            if image:
                project.image = image

            project.save()
            messages.success(request, 'Project edited successfully')
            return redirect('project_list')
        except Exception as e:
            messages.error(request, f'Error editing project: {e}')
            return redirect('project_edit', project_id=project.id) 

    context = {
        'current_page': current_page,
        'project': project
        }
    return render(request, 'admin_app/pages/project_edit.html', context)


@login_required(login_url='/auth/admin/login/')
def project_delete(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project_list')
    
    try: 
        project.delete()
        messages.success(request, 'Project deleted successfully')
        return redirect('project_list')
    except Exception as e:
        messages.error(request, f'Error deleting project: {e}')
        return redirect('project_list')

@login_required(login_url='/auth/admin/login/')    
def message_list(request):
    current_page = 'message_list'
    messages = Message.objects.all().order_by('-id')
    context = {
        'current_page': current_page,
        'messages': messages
        }
    return render(request, 'admin_app/pages/message_list.html', context)


@login_required(login_url='/auth/admin/login/')
def message_view(request, message_id):
    current_page = 'message_view'
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        messages.error(request, 'Message not found')
        return redirect('message_list')
    context = {
        'current_page': current_page,
        'message': message
        }
    return render(request, 'admin_app/pages/message_view.html', context)