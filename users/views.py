from django.shortcuts import render,redirect
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Import login_required decorator
# Create your views here.


def register(request): #define the method to register a user into the database
    if request.method =='POST': #if the form become submitted
        form = UserRegisterForm(request.POST) #create an instance of a form
        if form.is_valid():#check is the form created is valid?
            form.save() #yes its valid then save it to database
            username = form.cleaned_data.get('name')
            messages.success(request,f'Account created for {username}!')#displays message when account is created
            return redirect('login')#return to the main page

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required # Require user logged in before they can access profile page
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html',context)