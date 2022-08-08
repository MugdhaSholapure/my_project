from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from my_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

# Create your views here.
def user_signup(request):
	#if request.POST.get("un") and request.POST.get("em"):
	if request.method == "POST":
		print("hello")
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			#usr1 = User.objects.get(username=un)
			usr = User.objects.get(email=em)
			#print("usr1 = ",usr1)
			print("usr = ",usr)
			return render(request,"user_signup.html",{"msg":"Email already registered."})
			#elif usr2:
				#return render(request,"user_signup.html",{"msg":"Username already registered."})
				
		except User.DoesNotExist:
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(5):
				pw = pw + text[randrange(len(text))]
			print(pw)
			sub = "Welcome to myDaily Task " + str(un)
			msg = "You password is " + str(pw)
			sender = EMAIL_HOST_USER
			rvr = [str(em)]
			send_mail(sub,msg,sender,rvr)
			usr = User.objects.create_user(username=un,email=em,password=pw)
			usr.save()
			return redirect("user_login")
	

	else:						
		return render(request,"user_signup.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,"user_login.html",{"msg":"Invalid Login"})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"user_login.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def about(request):
	return render(request,"about.html")

def user_np(request):
	if request.method == "POST":
		em = request.POST.get("em")
		un = request.POST.get("un")
		try:
			usr = User.objects.get(email=em)
			email = usr.email
			print("usr = ",usr)
			print("email = ",email)
			if usr:
				pw = ""
				text = "abcdefghijklmnopqrstuvwxyz123456789"
				for i in range(5):
					pw = pw + text[randrange(len(text))]
				print(pw)
				sub = "Welcome to myDaily Task " + str(usr)
				msg = "Your new password is " + str(pw)
				sender = EMAIL_HOST_USER
				rvr = [str(em)]
				send_mail(sub,msg,sender,rvr)
				usr.set_password(pw) 
				usr.save()
				return redirect("user_login")
			
				
		except User.DoesNotExist:
			return render(request,"user_signup.html",{"msg":"Email not registered."})
	else:						
		return render(request,"user_np.html")

	


'''	 
	elif request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		pw = request.POST.get("pw")
		try:
			usr1 = User.objects.get(username=un)
			usr2 = User.objects.get(email=em)
			print("usr1 = ",usr1)
			print("usr2 = ",usr2)
			if usr1:
				return render(request,"user_signup.html",{"msg":"Username already registered."})
			elif usr2:
				return render(request,"user_signup.html",{"msg":"Email already registered."})
		except User.DoesNotExist:
			usr = User.objects.create_user(username=un,email=em,password=pw)
			usr.save()
			return redirect("user_login")
'''
