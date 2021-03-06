from blog.forms import PostForm
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages



# Create your views here.
def post_list(request):
    # print(request.user)
    # print(request.user.is_authenticated)
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

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post) #post.get_absolute_url

    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form':form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post) #post.get_absolute_url

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form':form,
    })