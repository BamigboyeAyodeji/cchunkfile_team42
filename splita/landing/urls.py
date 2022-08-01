from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]