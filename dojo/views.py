from django.shortcuts import render, redirect
from django.conf import settings
import os
# Create your views here.

from django.http import JsonResponse, HttpResponse
from dojo.forms import PostForm
from dojo.models import Post


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            # return redirect('/dojo/')

            post = Post(title= form.cleaned_data[title],
                        content = form.cleaned_data['content'])
            post.save()

            # post = Post.objects.create()
            # post = Post.objects.create(**form.cleaned_data)
    else:
        form = PostForm()
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