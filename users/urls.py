from django.urls import path
from . import views
from django.contrib.auth.views import login
app_name='users'
urlpatterns = [
    path('login/',login,{'template_name':'users/login.html'}, name ='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
]
