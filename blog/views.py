from django.shortcuts import render, get_object_or_404
from .models import BlogModel
from django.core.paginator import Paginator

def all_blogs(request):
    blogmodelobjects = BlogModel.objects.order_by('-blog_time')
    paginator = Paginator(blogmodelobjects,5)

    page = request.GET.get('page')

    blogmodelobjects = paginator.get_page(page)



    return(render(request,'blog/all_blogs.html',{'blogobjects':blogmodelobjects}))


def detail(request, blog_id):
    blog= get_object_or_404(BlogModel,pk = blog_id)
    return(render(request,'blog/detail.html',{'blog':blog}))