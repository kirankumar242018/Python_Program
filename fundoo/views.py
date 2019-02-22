import jwt as jwt
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import response, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.core.cache import cache


# from fundoo_app import api

from rest_framework.settings import api_settings

from .tokens import account_activation_token
from .forms import UserRegistrationForm
from django.shortcuts import render, HttpResponse, redirect
from rest_framework import generics

from . import models
from . import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    return render(request, 'fundoo/login.html')  # renders the login page


def index(request):
    return render(request, 'fundoo/index.html')  # renders the index page


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # registration by post method
        if form.is_valid():                        # checking for a validations
            user = form.save(commit=False)         # saving the form after validation
            user.is_active = False                 # initializing user active false
            user.save()                            # save the form to db
            current_site = get_current_site(request)
            message = render_to_string('fundoo/account_active_email.html', {
                'user': user,
                'domain': 'http://127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })  # encoding the information and attaching the token to header

            mail_subject = 'Activate your account..'     # mail subject is activate mail account
            to_email = form.cleaned_data.get('email')    # sending mail to the user entered mail address
            email = EmailMessage(mail_subject, message, to=[to_email])  # with message sending to the email
            email.send()
            messages.success(request, f'Please confirm your email to complete Registration process')
            # once sent confirm mail
            # return redirect('fundoo/account_active_sent_email.html')

            return HttpResponse("please confirm your email address to complete registration process..")   # giving response link has been sent
    else:
        form = UserRegistrationForm()  # re register correctly

    return render(request, 'fundoo/register.html', {'form': form})  # rendering back to register form


def user_login(request):
    res = {
        'message': 'Something went wrong',
        'data': {},
        'success': False
    }
    try:
        username = request.POST.get('username')  # getting information from post method
        password = request.POST.get('password')  # getting information from post method

        if username is None or password is None:  # fields should not be blank
            raise Exception("username or password filed should not be None...\n")
        user = authenticate(username=username, password=password)  # authenticating fields values
        print('username', user, username, password)   # printing the information
        if user:                                      # if a valid user
            if user.is_active:                        # and user is active
                login(request, user)                   # login into the page
                payload = {
                    'username': username,   # payload information
                    'password': password    # payload information
                }
                # generating jwt_token using algorithm HS256
                jwt_token = {'token': jwt.encode(payload, "secret_key", algorithm='HS256').decode()}
                j_token = jwt_token['token']
                res['message'] = "Welcome You Are Logged Successfully.."  # printing the message
                res['success'] = True                        # initialize to True
                cache.set('token', "token")                  # printing the data in  cache set
                res['data'] = j_token                         # storing data token
                print(res)                                     # printing the result
                return render(request, 'fundoo/index.html', {"token": res})  # after successful login render to index.
            else:
                return HttpResponse(messages.success(request, "your account is inactive"))  # else print account is inactive

        else:
            res['message'] = 'username or password is not correct'  # username or password invalid entry
            messages.error(request, 'invalid username or password')  # printing invalid entry
            return render(request, 'fundoo/login.html', context=res)   # render back to login page

    except Exception as e:   # handling exception
        print(e)
        return render(request, 'fundoo/login.html', context=res)

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # if username is None or password is None:
    #     #     raise Exception("username or  password field should not be None..\n")
    #
    #     user = authenticate(username=username, password=password)
    #     #user = User.objects.get(username=username, password=password)
    #     print('username', user, username, password)
    #
    #     if user:
    #         if user.is_active:
    #             login(request, user)
    #             jwt_token = get_jwt_token(user)
    #             # url = ''
    #             #jwt_token
    #             response['Token'] = jwt_token
    #             return render(request,'fundoo/index.html',{})
    #         else:
    #             return HttpResponse(messages.success(request, "your account is inactive"))
    #
    #     else:
    #         messages.success(request, f'Invalid username or password')
    #         # return render(request,'fundoo/home.html',{})
    #         return redirect('user_login')
    # else:
    #     messages.success(request, f'you are forget to enter username and password..\n')
    #     return render(request, 'fundoo/login.html', {})


def get_jwt_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    print(payload)
    print(jwt_encode_handler(payload))

    return jwt_encode_handler(payload)


def activate(request, uidb64, token):
    """
    :param request: Http request
    :param uidb64: user's id encoded in base 64
    :param token: generated token for user
    :return: http response with text message
    """
    try:
        # takes user id and generates the base64 code
        uid = force_text(urlsafe_base64_decode(uidb64))
        # get user for given uid
        print(uid)
        user = User.objects.get(pk=uid)
        print(user)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        # check user is not null and has a token
    if user is not None and account_activation_token.check_token(user, token):

        user.is_active = True   # make user active
        user.save()   # save user
        login(request, user)  # make request for login
        messages.success(request, f'Thank you for your email confirmation. Now you can login your account.')
        return redirect('user_login')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        # messages.success(request, f'Activation link is invalid!.')
        return HttpResponse('Activation link is invalid!')
    # return redirect('user_login')

#
# class UserListView(generics.ListCreateAPIView):
#     queryset = models.CustomUser.objects.all()
#     serializer_class = serializers.UserSerializer
