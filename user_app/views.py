from django.shortcuts import render, redirect
from django.contrib import messages
from admin_app.models import Message, Project
# Create your views here.

def home(request):
    current_page = 'home'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/home.html', context)

def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/about.html', context)

def services(request):
    current_page = 'services'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/services.html', context)

def projects(request):
    current_page = 'projects'
    compleated_projects = Project.objects.filter(status=True)
    ongoing_projects = Project.objects.filter(status=False)
    context = {
        'current_page': current_page,
        'compleated_projects': compleated_projects,
        'ongoing_projects': ongoing_projects,
    }
    return render(request, 'user_app/pages/projects.html', context)

def contact(request):
    current_page = 'contact'
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message') 

        try:
            message = Message(
                name=name,
                email=email,
                message=message,
            )
            message.save()
            messages.success(request, 'Message send successfully')
            return redirect('contact')  
        except Exception as e:
            messages.error(request, f'Error adding message: {e}')
            return redirect('contact')  
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/contact.html', context)




    


    