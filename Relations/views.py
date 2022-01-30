import email
from django.shortcuts import render, reverse
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
       

def Sign_up(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email)
            user.save()
            profile = Profile(user = user)
            profile.save()
            msg = f"{username}'s account has been created successfully"
            return render(request, 'relations/sign_up.html', {'form' : form, 'msg' : msg})

    return render(request, 'relations/sign_up.html', {'form' : form})

class Signin(forms.Form):
    username = forms.CharField(max_length=35, label = 'username or email')
    password = forms.CharField(max_length= 15, widget=forms.PasswordInput)

def Sign_in(request):
    form = Signin()
    msg = None
    if request.method == 'POST':
        form = Signin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = User.objects.filter(Q(username = username)| Q(email = username)).first()
            if user:
                if user.check_password(password):
                    login(request, user)
                    return HttpResponseRedirect(reverse('App_in', args = []))
                else:
                    msg = f"{username}, your password is wrong"
            else:
                msg = f"{username} not found"
    return render(request, 'relations/sign_in.html', {'form' : form, 'msg' : msg})

class appin_form(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'friends']

def appin(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user)

        form = appin_form(instance=profile)
        if request.method == 'POST':
            form = appin_form(request.POST, files=request.FILES, instance=profile)
            if form.is_valid():
                form.user = request.user
                form.save()
        return render(request, 'relations/appin.html', {'form' : form})
    
class search(forms.Form):
    Search = forms.CharField(max_length=30)

def add_friend(request):
    form = search()
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            searched = form.cleaned_data['Search']
            users = User.objects.filter(username__icontains = searched).all()
            return render(request, 'relations/addfriend.html', {'form' : form, 'users' : users})
    return render(request, 'relations/addfriend.html', {'form' : form})
        
def Add(request, Id):
    user = User.objects.filter(id = Id).first()
    userprofile = Profile.objects.filter(user=request.user).first()
    Friends = userprofile.friends.all()
    if user in Friends:
        return HttpResponse(f'{user} already in friend list')
    else:
        userprofile.friends.add(user)
        userprofile.save()
        return HttpResponse(f'{user} added to friend list')

def showfriends(request):
    all_friends = request.user.profile.friends.all()