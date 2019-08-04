from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile),
]