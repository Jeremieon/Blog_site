from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Import login_required decorator
# Create your views here.

def register(request): #define the method to register a user into the database
    if request.method =='POST': #if the form become submitted
        form = UserRegisterForm(request.Post) #create an instance of a form
        if form.is_valid():#check is the form created is valid?
            form.save() #yes its valid then save it to database
            username = form.cleaned_data.get('name')
            messages.sucess(request,f'Account created for {username}!')#displays message when account is created
            return redirect('login')#return to the main page

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required # Require user logged in before they can access profile page
def profile(request):
    return render(request, 'users/profile.html')