from django.urls import path
from . import views


urlpatterns = [
	path('signin/', views.loginPage, name="signin"),  
	path('signup/', views.registerPage, name="signup"),
	path('signout/', views.logoutUser, name="signout"),
]