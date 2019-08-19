from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from upload.models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from PIL import Image

import pytesseract
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def index(request):
    return HttpResponse("<h1>Upload page</h1>")

def display(request):
    return HttpResponse("<h1>Display and edit data page</h1>")

def displayhtml(request):
    return render(request, 'Testing/post_html.html', {})

def post_new(request):
    '''form = PostForm()
    return render(request, 'Testing/post_edit.html', {'form': form})'''
    print("save button clicked")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print("This is post title:",post.title)
            print("This is post content:", post.text)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('displayhtml')
            return redirect('post_detail', pk=post.pk)
            #return render(request, 'Testing/post_detail.html',  post)
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
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Testing/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print("This is post title ", post.title)
    return render(request, 'Testing/post_detail.html', {'post': post})

def upload_file(request):
    print("Button pressed")
    if request.method == 'POST':
        uploaded_file= request.FILES['document']
        print("This is uploaded file name:", uploaded_file.name, " file size:",uploaded_file.size)
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image, lang="eng").splitlines()
        print("This is the text:",text)

    return render(request, 'Testing/upload.html')