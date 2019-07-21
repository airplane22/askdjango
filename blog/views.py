from django.http import Http404
from django.shortcuts import render, get_object_or_404
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

def post_detail(request, id):
#    try:
#        post = Post.objects.get(id=id)
#
#    except Post.DoesNotExist:
#        raise Http404

    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post':post,
    })

