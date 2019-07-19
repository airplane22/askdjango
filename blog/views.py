from django.shortcuts import render
from .models import Post



# Create your views here.
def post_list(request):
    qs = Post.objects.all() #아직 DB 접속 이루어지지 않음
    return render(request, 'blog/post_list.html',{
        'post_list':qs,
    })