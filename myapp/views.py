from django.shortcuts import render, render_to_response
# from django.contrib.auth import authenticate

from myapp.auth_email import EmailOrUsernameModelBackend
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from myapp.forms import UserForm


# Create your views here.
def index(request):
	return render_to_response('index.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
				
		user = EmailOrUsernameModelBackend.authenticate(username, password)

		if user:
			if user.is_active:
				auth_login(request, user)
				# return HttpResponseRedirect(reverse('index'))
				return render(request, 'index.html', {})

			else:
				return HttpResponse("Your accounts was inactive.")

		else:
			print("Someone tried to login and failed.")
			print("They used username: {} and password: {}".format(username, password))
			
			return render(request, 'login.html', {})
	else:
		return render(request, 'login.html', {})
	


def signup(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)		
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			
			registered = True

			return render(request, 'index.html', {})

		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
		# profile_form = UserProfileInfoForm()

	return render(request, 'signup.html', {'user_form':user_form, 'registered':registered})



def dash(request):
	return render_to_response('dashboard.html')

