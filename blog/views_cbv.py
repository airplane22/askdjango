from .models import Post
from django import forms
from django.views.generic import CreateView, ListView, DetailView

post_list = ListView.as_view(model=Post, paginate_by =3)  # /?page=2 로 다음 페이지 넘어갈 수 있음

post_detail = DetailView.as_view(model=Post)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    #success_url = '/...'

post_new = PostCreateView.as_view()



#models.py 에서 get_absolute_url -- 자동으로 detail 화면으로 넘어감