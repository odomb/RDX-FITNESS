from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('Contact',views.Contact,name="Contact"),
    path('join',views.enroll,name="enroll"),
    
]
    