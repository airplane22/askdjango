#blog/urls.py

from django.urls import path
from . import views
from . import views_cbv

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<pk>', views_cbv.post_detail, name='post_detail'),
    path('<id>', views.post_detail, name='post_detail'),

    path('new/', views.post_new, name='post_new'),
    path('<int:id>/', views.post_edit, name='post_edit'),

    path('cbv/', views_cbv.post_list, name='post_list'),
    path('cbv/new/', views_cbv.post_new),
    path('cbv/<pk>/edit/', views_cbv.post_edit),
]