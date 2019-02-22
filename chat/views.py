from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import UserLoginAndRegister
import json
from django.utils.safestring import mark_safe


# from django.contrib.auth.forms import UserRegisterForm,


def base(request):
    return render(request, 'chat/base.html', {})


# def register(request):
#     form = UserRegister()
#     return render(request, 'chat/register.html', {'form': form})
#
#
# def signup(request):
#     form = UserSignup()
#     return render(request, 'chat/login_form.html', {'form': form})


def register_and_signup(request):
    form = UserLoginAndRegister()
    return render(request, 'chat/login_and_register.html', {'form': form})


def addUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    all_user = UserLoginAndRegister(username=username, email=email, password=password)
    all_user.save()
    return render(request, 'chat/login_and_register.html', {})


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


User = get_user_model()


def chat_login(request):

    if request.method == "POST":
        # all_user = UserLoginAndRegister.objects.all()
        # username = request.POST.get('username')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # user = authenticate(username='username', password='password')

        # user = User.objects.get(username=username, password=password)
        user=User.objects.filter(username=username, password=password).first()

        print(username, password)
        if user:
            return render(request, 'index.html')
        else:
           return  HttpResponse("No valid user")

    else: HttpResponse("GET request ")


def loginchatview(request):
    all_user = UserLoginAndRegister.objects.all()
    fname = request.POST['username']
    password = request.POST['password']
    print('in login view')
    for user in all_user:
        if user.username == fname and user.password == password:
            print(fname, password)
            return render(request, 'chat/index.html')
            #return HttpResponse("Logged in successfully")
    # return render(request, 'chat/login_and_register.html', {'error': "sorry,you are not a invalid user.."})

    return HttpResponse(" sorry,invalid username or password....!")