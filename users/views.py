from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def confirm_logout(request):
    """Render the confirmation logout page."""
    return render(request, 'registration/confirm_logout.html')

def register(request):
    """Register's a new user."""
    if request.method != "POST":
        # Display default django registration form.
        form = UserCreationForm()

    else:
        # Process the completed form for registration and login.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in new user then redirect to home page. 
            login(request, new_user)
            return redirect('loggs:index')
        
    # Display a blank or invalid form. 
    context = {'form': form}
    return render(request, 'registration/register.html', context)


