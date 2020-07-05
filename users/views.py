from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def register(request):
    if request.method != 'POST':
        # Create a blank form
        form = UserCreationForm()
    else:
        # Process the data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            login(request, new_user)
            return redirect('users:login')

    # Display the data or not
    return render(request, 'registration/register.html', {'form': form})
