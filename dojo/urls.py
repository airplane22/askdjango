from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    #path('hello/<str:name>/<int:age>/', views.hello), #repath로 ㄱ-힣으로 name 한글 문자열 매칭으로 바꾸기!!
    re_path(r'^hello/(?P<name>[ㄱ-힣/]+)/(?P<age>[\d]+)/$', views.hello),
    path('post_list1/', views.post_list1),
    path('post_list2/', views.post_list2),
    path('post_list3/', views.post_list3),
    path('excel/', views.excel_download),

]