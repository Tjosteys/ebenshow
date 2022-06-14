from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegForm

# Create your views here.
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					# return HttpResponse('Authenticated successfully')
					return render(request, 'shoprite/base.html')
				else:
					return HttpResponse('This account has been disabled')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form':form})


def register(request):
	if request.method == 'POST':
		user_form = UserRegForm(request.POST)
		if user_form.is_valid():
			#create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			#set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			#save the user object
			new_user.save()
			#create the user profile
			# return render(request, 'shoprite/product/list.html')
			# Profile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user':new_user})
	else:
		user_form = UserRegForm()
	return render(request, 'account/register.html', {'user_form':user_form})

def logged_out(request):
	return render(request, 'account/logged_out.html')