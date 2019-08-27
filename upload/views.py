from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from upload.models import Post
from .forms import *
from django.utils import timezone
from django.shortcuts import redirect
from PIL import Image
from .ImageToText import  *
from django.urls import reverse
from urllib.parse import urlencode


import pytesseract

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
        print("line 33 form is ",form)
        print("line 34 form type is ", type(form))
        if form.is_valid():
            post = form.save(commit=False)
            print("This is post title line 35:",post.title)
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

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print("This is post title ", post.title)
    return render(request, 'Testing/post_detail.html', {'post': post})
    #return render(request, 'Testing/post_detail.html', {'form': form})

def post_results(request):
    #context= get_object_or_404(BloodSamples,pk=pk)
    if request.method == 'POST':
        print("line 74 clicked")
        Bloodform = BloodSampleForm(request.POST)
        print ("Bloodform line 76:",Bloodform)
        print("Bloodform line 77:", type(Bloodform), Bloodform.errors)
        if Bloodform.is_valid():
            print ("BloodForm is valid")
            Bloodpost = Bloodform.save(commit=False)
            print("This is post title line 35:",Bloodpost.Sodium)
            print("This is post content:", Bloodpost.Potassium)
            print("Bloodform Date time is:", Bloodpost.Date_Time,"THE REQUEST POST:", request.POST)


    context = request.GET
    mydict = context.dict()
    print("debug at line 75:", type(mydict))
    BloodSample = BloodSampleForm(initial=mydict)
    args = {'BloodSamples': BloodSample}
    return render(request, 'Testing/post_results.html', args)


def upload_DB(request):
    print("In this loop line 82, the request method is ", request.method)

    if request.method == "POST":
        print("In this loop line 84")
        Bloodform = BloodSampleForm(request.POST)
        print("Bloodform Date time is:",Bloodform.Date_Time)



def upload_file(request):
    print("Button pressed line 92")
    if request.method == 'POST':
        uploaded_file= request.FILES['document']
        print("This is uploaded file name:", uploaded_file.name, " file size:",uploaded_file.size)
        object_img2txt = ImageToText(uploaded_file)
        object_img2txt_output = object_img2txt.ReturnObject()
        print("THis is the output line 98:",object_img2txt_output[0])
        print(type(object_img2txt_output[0]))
        BloodSample = BloodSampleForm(initial=object_img2txt_output[0])
        args = {'BloodSamples': BloodSample}  # can pass in multiple args not use for now
        # can have all the field in the database then selectively choose, can use "if" see post_details.html
        base_url = reverse('post_results')
        query_string = urlencode(object_img2txt_output[0])
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)


    return render(request, 'Testing/upload.html')

def login(request):
    print("Button pressed line 125")

    if request.method == "POST":
        form = LoginForm(request.POST)
        loginpost = form.save(commit=False)
        print("Button pressed line 127:",request.POST)
        if(loginpost.username=='mecfs' and loginpost.password=='mecfs'):
            print("Correct password")
            return redirect(upload_file)
    else:
        form = LoginForm()
    return render(request, 'Testing/login.html',{'form':form})


