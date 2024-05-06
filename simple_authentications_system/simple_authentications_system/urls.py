
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("author.urls")),
    path("",views.Home,name="Home_page")
]
