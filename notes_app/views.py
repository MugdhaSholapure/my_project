from django.shortcuts import render,redirect
from .models import NotesModel
import requests
#from my_project.auapp.views import User

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("about")

def add_notes(request):
	if request.method == "POST":
		user = request.user
		print(user)
		title = request.POST.get("title")
		deadline = request.POST.get("deadline")
		description = request.POST.get("description")
		'''
		try:
			task = NotesModel.object.get(title=title)
			return render(request,"add_notes.html",{"msg":"Task already exists."})
		except NotesModel.DoesNotExist:
		'''
		task = NotesModel(user=user,title=title,deadline=deadline,description=description)
		task.save()
		#return redirect("view_notes")
		return render(request,"add_notes.html",{"msg":"Task added."})
	else:
		return render(request,"add_notes.html")
	

def view_notes(request):
	#user = NotesModel.objects.all()
	#print (user)
	#print(NotesModel.object.get(user = username))
	task = NotesModel.objects.filter(user=request.user)
	#print(task)
	#task = list(task)
	return render(request,"view_notes.html",{"task":task})
	

def delete_task(request,id):
	task = NotesModel.objects.get(SrNo = id)
	task.delete()
	return redirect("view_notes")


def edit_task(request,id):
	if request.method == "POST":
		user = request.user
		task = NotesModel.objects.get(SrNo = id)
		SrNo = id
		title = request.POST.get("title")
		deadline = request.POST.get("deadline")
		description = request.POST.get("description")
		if task is None:
			return redirect("view_notes")
		else:
			task = NotesModel(user=user,SrNo=SrNo,title=title,deadline=deadline,description=description)
			task.save()
			return redirect("view_notes")
	
	elif request.POST.get("back"):
		return redirect("edit_task")		
	else:
		task = NotesModel.objects.get(SrNo = id)
		print (task)
		return render(request,"edit_task.html",{"data":task})
		#return redirect("edit_task")

def check_weather(request):
	#if request.POST.get("city") and request.POST.get("btn"):
	if request.method == "POST":
		city = request.POST.get("city")
		try:
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric" 
			a2 = "&q=" + city
			a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
			wa = a1 + a2 + a3
			res = requests.get(wa)
			data = res.json()
			temp = data['main']['temp']
			desc = data['weather'][0]['description']
			msg = " City = " + city + "\n Temp = " + str(temp) + " °C " + "\n Desc = " + desc
			icon = "http://api.openweathermap.org/img/w/" + data['weather'][0]['icon'] + ".png"
			return render(request,"check_weather.html",{"msg":msg,"icon":icon})
		except Exception as e:
			return render(request,"check_weather.html",{"msg":str(e) + str("Invalid City Name")})
	else:
		return render(request,"check_weather.html")
	