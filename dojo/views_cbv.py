# from django.views.generic import View  re_path
# from django.http import HttpResponse
#
# class PostListView1(View):
#     def get(self, request):
#         name = '공유'
#         html = self.get_template_string().format(name = name)
#         return HttpResponse(html)
#         return #4강 26분부터!!!
#
#     def get_template_string(self):
#         return '''
#             <h1>AskDjango</h1>
#             <p>{name}</p>
#             <p>여러분의 파이썬 장고 페이스메이커</p>
#         '''
#
# post_list1 = PostListView1.as_view()
#
# class PostListView2(TemplateView):
#     template_name = 'dojo/post_list.html'
#
# post_list2 = PostListView2.as_view()
#
# class PostListView3(object):
#     pass
#
# class ExcelDownloadView(object):
#     pass



