from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from upload.models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return HttpResponse("<h1>Upload page</h1>")

def display(request):
    return HttpResponse("<h1>Display and edit data page</h1>")

def displayhtml(request):
    return render(request, 'Testing/post_list.html', {})

def post_new(request):
    '''form = PostForm()
    return render(request, 'Testing/post_edit.html', {'form': form})'''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print("This is post title:",post.title)
            print("This is post content:", post.text)
            ##post.author = request.user
            post.published_date = timezone.now()
            ##post.save()
            return redirect('Testing/post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Testing/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            ##post.author = request.user
            post.published_date = timezone.now()
            ##post.save()
            return redirect('Testing/post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Testing/post_edit.html', {'form': form})

def post_detail(request,post):
    return redirect('post_detail', pk=post.pk)