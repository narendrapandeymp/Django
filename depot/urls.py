from django.contrib import admin
from django.urls import path,include
from depot import views

urlpatterns = [ path("", views.index, name= 'depot'),
    path("about", views.about, name= 'about'),
    path("ok", views.ok, name= 'ok'),
    path("px", views.px, name= 'px'),
    path("login",views.login, name="login")
]
