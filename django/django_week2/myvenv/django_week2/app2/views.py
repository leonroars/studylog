from django.shortcuts import render, get_object_or_404, redirect # get_object_or_404 = 객체를 가져올 때 있으면 걔를 가져오고 없으면 404 return
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, pk=id) #'Blog' 라는 이름을 가진 객체 중에 pk값이 내가 지정한 id값과 같은 것을 호출
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def update(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('detail', blog.id)
    return render(request, 'update.html', {"blog" : blog})

def delete(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return redirect('home')
    


# Create your views here.
