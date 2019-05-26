from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UserRegisterForm

# Create your views here.


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'home.html', context)


def register(request):
   if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Your account has been created! You are now able to log in')
           return redirect('login')
   else:
       form = UserRegisterForm()
   return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')