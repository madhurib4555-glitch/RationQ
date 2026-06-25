from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login')

    return render(request, 'register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard')

    return render(request, 'login.html')


from queue_system.models import QueueToken

def dashboard(request):

    total_tokens = QueueToken.objects.count()

    waiting_tokens = QueueToken.objects.filter(
        status='Waiting'
    ).count()

    completed_tokens = QueueToken.objects.filter(
        status='Completed'
    ).count()

    current_token = QueueToken.objects.filter(
        status='Waiting'
    ).order_by('created_at').first()

    context = {
        'total_tokens': total_tokens,
        'waiting_tokens': waiting_tokens,
        'completed_tokens': completed_tokens,
        'current_token': current_token
    }

    return render(
        request,
        'dashboard.html',
        context
    )

def user_logout(request):

    logout(request)

    return redirect('/')