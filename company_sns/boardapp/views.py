from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', { 'error': 'このユーザーは登録されています' })
        except:
            user = User.objects.create_user(user_name, '', password)
            return render(request, 'signup.html', { 'some': 100 })
    return render(request, 'signup.html', { 'some' :100 })