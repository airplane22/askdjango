from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import os
# Create your views here.

from django.http import JsonResponse, HttpResponse
from dojo.forms import PostForm
from dojo.models import Post
from django.views.generic import DetailView

#step5
post_detail = DetailView.as_view(model=Post)
# urls.py 에서 id를 pk로 수정

# step4
# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')  #pk_url_kwarg : path에서 전달받을 인자의 이름 path('<int:id>/'일 때 id)


# step3
# class DetailView(object):
#     def __init__(self, model):
#         self.model = model
#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(self.model, id=kwargs['id'])
#     def get_template_name(self):
#         return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
#     def dispatch(self, request, *args, **kwargs):
#         return render(request, self.get_template_name(), {
#             self.model._meta.model_name: self.get_object(*args, **kwargs),
#         })
#     @classmethod
#     def as_view(cls, model):
#         def view(request, *args, **kwargs):
#             self = cls(model)
#             return self.dispatch(request, *args, **kwargs)
#         return view
#
# post_detail = DetailView.as_view(Post)  #CBV

# step2
# def generate_view_fn(model):
#     def view_fn(request, id):
#         instance = get_object_or_404(model, id=id)
#         instance_name = model._meta.model_name  #모델이름 소문자
#         template_name = '{}/{}_detail.html'.format(model._met.app_label, instance_name) #모델이 포함된 앱이름
#         return render(request, template_name, {
#             instance_name: instance,
#         })
#     return view_fn
#
# post_detail = generate_view_fn(Post)  #generate_view_fn 에서 나온 함수!

# step1.
# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'dojo/post_detail.html', {
#         'post':post,
#     })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            # return redirect('/dojo/')

            # 방법2
            # post = Post(title= form.cleaned_data[title],
            #             content = form.cleaned_data['content'])
            # post.save()

            # 방법3 post = Post.objects.create()
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form':form
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post) #instance = post!!
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form':form
    })

def mysum(request, numbers):
    #numbers = "1/12/123/12/123"
    result = sum(map(lambda s : int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name, age))

def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커</p>
    '''.format(name=name))

def post_list2(request):
    name = '공유'
    return  render(request, 'dojo/post_list.html', {'name': name})

def post_list3(request):
    return JsonResponse({
    'message':'안녕 파이썬 장고',
    'items' : ['파이썬', '장고','Celery','Azure','Aws']
    }, json_dumps_params={'ensure_ascii':False})

def excel_download(request):
    # filepath = 'c:\dev\djbasic_practice.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'djbasic_practice.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename = "{}"'.format(filename)
        return response