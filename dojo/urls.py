from django.urls import path,re_path
from . import views
from . import views_cbv

urlpatterns = [
    path('new/', views.post_new),
    path('<int:id>', views.post_detail),
    path('<int:id>/edit/', views.post_edit),

    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    #path('hello/<str:name>/<int:age>/', views.hello), #repath로 ㄱ-힣으로 name 한글 문자열 매칭으로 바꾸기!!
    re_path(r'^hello/(?P<name>[ㄱ-힣/]+)/(?P<age>[\d]+)/$', views.hello),
    path('post_list1/', views.post_list1),
    path('post_list2/', views.post_list2),
    path('post_list3/', views.post_list3),
    path('excel/', views.excel_download),

    # path('cbv/post_list1/', views_cbv.post_list1),
    # path('cbv/post_list2/', views_cbv.post_list2),
    # path('cbv/post_list3/', views_cbv.post_list3),
    # path('cbv/excel/', views_cbv.excel_download),


]