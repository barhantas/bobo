from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.generic import View
from .models import User, Place
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse
from .forms import UserForm, LoginForm,SettingsForm,MessageForm,PlaceForm,ProfilePic



def indexvisitor(request):
    all_users = User.objects.all()
    context = {'all_users': all_users}
    return render(request, 'user/base_visitor.html', context)


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'user/login.html')
    else:
        #form = User.objects.all().values_list('geo_loc').filter(geo_loc__iregex="\\d\\d*.*,\\d*.\\d*\\d")
        form = User.objects.all().values_list('geo_loc',flat=True).filter(geo_loc__icontains=",")[:1].get()
        formtester = User.objects.all().values_list('geo_loc', flat=True).filter(geo_loc__icontains=",")
        formtest = User.objects.all().values_list('geo_loc' ,'message','profile_pic').filter(geo_loc__icontains=",")
        message = User.objects.all().values_list('message',flat=True).filter(message__iregex="[^(?:''), ]\w*\s*\d*")

        return render(request, 'user/index.html', {'form': form, 'message': message, 'formtest': formtest,'formtester':formtester })

def profile(request,id=None):
    if not request.user.is_authenticated():
        return render(request, 'user/login.html')
    else:
        if request.method == 'POST':
            form = MessageForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                return redirect(reverse('profile'))
        else:
            form = MessageForm(instance=request.user)
            args = {'form': form}
            return render(request, 'user/profile.html', args)
     #return render(request, 'user/profile.html')

def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST,request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = SettingsForm(instance=request.user)
        args = {'form': form}
        return render(request, 'user/settings.html', args)

# def settings(request):
#     if not request.user.is_authenticated():
#         return redirect('index')
#     else:
#         user = User.objects.get(pk=request.user.id)
#         form = ProfilePic(request.POST or None,initial={'profile_pic': user.profile_pic})
#         if request.method == 'POST':
#             if form.is_valid():
#                 user.profile_pic = request.POST['profile_pic']
#                 user.save()
#                 return redirect('profile')
#
#         context = {
#             "form": form
#         }
#         return render(request, "user/settings.html", {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                users = User.objects.filter(username=request.user)
                return render(request, 'user/index.html', {'users': users})
            else:
                return render(request, 'user/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'user/login.html', {'error_message': 'Invalid login'})
    return render(request, 'user/login.html')

def logout_user(request):
    logout(request)
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('index')


class UserLoginView(View):
    form_class = LoginForm
    template_name = "user/login.html"

    def get(self,request):
        form = self.form_class(None)
        if request.user.is_authenticated():
            return redirect('index')
        else:
         return render(request, self.template_name , {'form': form})

    def post(self,request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'user/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'user/login.html', {'error_message': 'Invalid login'})
        return render(request, 'user/login.html')




# class UserFormView(View):
#     form_class = UserForm
#     template_name = "user/registration_form.html"
#
#     #display blank form
#     def get(self,request):
#
#         if not request.user.is_authenticated():
#             form = self.form_class(None)
#             return render(request, self.template_name, {'form': form})
#         else:
#             return redirect('index')
#     #process form data
#     def post(self,request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit=False)
#
#             #normalized data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             #user.set_password(password)
#             user.save()
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('indexlogged')
#
#
#
#         return render(request, 'user/base.html' , {'form': form})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'user/registration_form.html', context)