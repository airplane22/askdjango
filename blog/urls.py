#blog/urls.py

from django.urls import path
from . import views
from . import views_cbv

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<id>', views.post_detail, name='post_detail'),

    path('cbv/new/', views_cbv.post_new)
]