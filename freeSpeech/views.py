from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserCreateForm

def sign_in(request):
    if request.method =="POST":
        form.UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.username
            user.email = request.email
            user.password = request.password1
            user.save
            return redirect('welcome')
    else:
        form = UserCreateForm()

    return render(request, 'sign_in.html', {'form': form})
