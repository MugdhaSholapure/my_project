
from django.contrib import admin
from django.urls import path, re_path,include,re_path
from notes_app.views import home,add_notes,view_notes,delete_task,edit_task,check_weather
from auapp.views import user_login,user_signup,user_logout,about,user_np

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("user_login/",user_login,name="user_login"),
    path("user_signup/",user_signup,name="user_signup"),
    path("user_logout/",user_logout,name="user_logout"),
    path("user_np/",user_np,name="user_np"),
    path("about/",about,name="about"),
    path("add_notes/",add_notes,name="add_notes"),
    path("view_notes/",view_notes,name="view_notes"),
    path("delete_task/<int:id>",delete_task,name="delete_task"),
    path("edit_task/<int:id>",edit_task,name="edit_task"),
    path("check_weather/",check_weather,name="check_weather"),	   
]
