from django.shortcuts import render
from .models import Post



# Create your views here.
def post_list(request):
    qs = Post.objects.all() #아직 DB 접속 이루어지지 않음


##q 인자 가져오는법 다시보기!!!
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html',{
        'post_list':qs,
        # 'q'=q, ??? 9강 25:00
    })