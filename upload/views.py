from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.utils import timezone
from django.shortcuts import redirect
from .ImageToText import *
import DBAccessKey
from .LoginCheck import *

# Create your views here.
access_key_id_global = DBAccessKey.DBAccessKey.access_key_id_global
secret_access_key_global = DBAccessKey.DBAccessKey.secret_access_key_global


def index(request):
    return HttpResponse("<h1>Upload page</h1>")


def display(request):
    return HttpResponse("<h1>Display and edit data page</h1>")


def displayhtml(request):
    return render(request, 'Testing/post_html.html', {})


def post_new(request):
    '''form = PostForm()
    return render(request, 'Testing/post_edit.html', {'form': form})'''

    if request.method == "POST":
        print("This is the request.post:", request.POST)
        if request.POST.get("save"):
            form = PostForm(request.POST)
            print("line 33 form is ", form)
            print("line 34 form type is ", type(form))
            if form.is_valid():
                post = form.save(commit=False)
                print("This is post title line 35:", post.title)
                print("This is post content:", post.text)
                # post.author = request.user
                post.published_date = timezone.now()
                post.save()
                # #return redirect('displayhtml')
                return redirect('post_detail', pk=post.pk)
        elif request.POST.get("displayhtml"):
            print("In displayHTML loop")
            return redirect(displayhtml)
            # return render(request, 'Testing/post_detail.html',  post)
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
    # return render(request, 'Testing/post_detail.html', {'form': form})


def post_results(request):
    # context= get_object_or_404(BloodSamples,pk=pk)
    if request.method == 'POST':
        print("line 74 clicked")
        Bloodform = BloodSampleForm(request.POST)
        print("Bloodform line 76:", Bloodform)
        print("Bloodform line 77:", type(Bloodform), Bloodform.errors)
        if Bloodform.is_valid():
            print("BloodForm is valid")
            Bloodpost = Bloodform.save(commit=False)
            print("This is post title line 35:", Bloodpost.Sodium)
            print("This is post content:", Bloodpost.Potassium)
            print("Bloodform Date time is:", Bloodpost.Date_Time, "THE REQUEST POST:", request.POST)

    print("This is request.GET line89", request.GET)
    context = request.GET
    mydict = context.dict()
    if "HAEMOGLOBIN" in mydict:
        BloodSample = BloodSampleForm2(initial=mydict)
        print("in haemoglobin loop")
    elif "Potassium" in mydict:
        BloodSample = BloodSampleForm(initial=mydict)
        print("in Potassium loop")

    print("debug at line 75:", type(mydict))
    # BloodSample = BloodSampleForm(initial=mydict)
    args = {'BloodSamples': BloodSample}
    return render(request, 'Testing/post_results.html', args)


def upload_DB(request):
    print("In this loop line 82, the request method is ", request.method)

    if request.method == "POST":
        print("In this loop line 84")
        Bloodform = BloodSampleForm(request.POST)
        print("Bloodform Date time is:", Bloodform.Date_Time)


list_of_files = []
list_of_dict = []


def upload_file(request):
    login_checker = LoginCheck('Login', 'valid')
    if login_checker.check_login():
        if request.POST.get("upload_to_DB"):
            context = request.POST
            mydict = context.dict()

            # put the upload to db here
            upload_to_db(mydict)

            list_of_files.remove(request.POST.get("File_name"))

            if len(list_of_files) == 0:
                return render(request, 'Testing/upload.html')

            # show the next file that is pending to be uploaded
            for dict in list_of_dict:
                if dict[0]["File_name"] == list_of_files[0]:
                    args = {'button': list_of_files, 'form': returnform(dict[0])}
                    return render(request, 'Testing/display_table.html', args)

            args = {'button': list_of_files, 'form': returnform(mydict)}
            return render(request, 'Testing/display_table.html', args)

        if request.POST.get("upload"):
            list_of_dict.clear()
            list_of_files.clear()

            uploaded_file = request.FILES.getlist('document')

            btn_value = request.POST.get("upload", "")
            count = 0

            if btn_value != 'upload':
                for del_id in btn_value:
                    if del_id != ',':
                        print(del_id)
                        delete_idx = int(del_id) - count
                        uploaded_file.pop(delete_idx)
                        count += 1

            for file in uploaded_file:
                print("This is uploaded file name:", file.name, " file size:", file.size)
                list_of_files.append(file.name)
                object_img2txt = ImageToText(file)
                object_img2txt_output = object_img2txt.ReturnObject()
                list_of_dict.append(object_img2txt_output)

            args = {'button': list_of_files, 'form': returnform(object_img2txt_output[0])}
            return render(request, 'Testing/display_table.html', args)

        for file in list_of_files:
            if request.POST.get(file):
                for dict in list_of_dict:
                    filename = dict[0].get("File_name")
                    if dict[0]["File_name"] == file:
                        args = {'button': list_of_files, 'form': returnform(dict[0])}

                        return render(request, 'Testing/display_table.html', args)

            ## save entries in sql and then encode the url with the primary key
            # base_url = reverse('post_results')
            # query_string = urlencode(object_img2txt_output[0])
            # url = '{}?{}'.format(base_url, query_string)
            # return redirect(url)

        return render(request, 'Testing/upload.html')
    else:
        return HttpResponse("<h1>No Login</h1>")



def returnform(dictionary):

    if "HAEMOGLOBIN" in dictionary:
        BloodSample = BloodSampleForm2(initial=dictionary)

    elif "Lymphocytes" in dictionary:
        BloodSample = BloodSampleForm2(initial=dictionary)

    elif "Potassium" in dictionary:
        BloodSample = BloodSampleForm(initial=dictionary)

    elif "Parathyroid_Hormone" in dictionary:
        BloodSample = BloodSampleForm3(initial=dictionary)

    elif "Vitamin_D" in dictionary:
        BloodSample = BloodSampleForm4(initial=dictionary)

    return BloodSample


def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        loginpost = form.save(commit=False)

        login_checker = LoginCheck(loginpost.username, loginpost.password)
        if login_checker.check_login():
            print("Correct password")
            update_Login_db('ff8858b7266f7d36585de94e854f4778') #code for valid
            return redirect(upload_file)
        else:
            update_Login_db('1') #code for invalid
            return HttpResponse("<h1>No Login</h1>")

    else:
        form = LoginForm()
    return render(request, 'Testing/login.html', {'form': form})


def display_table(request):
    # save it in the sql database, use dictionary, then url encode the primary key, then retriev it from this side
    button = ['red', 'blue', 'green']
    print("This is request.post", request.POST)
    form = null()
    if request.POST.get("red"):
        print("In the red loop")
        form = BloodSampleForm2()
    elif request.POST.get("green"):
        print("In the green loop")
        form = BloodSampleForm()

    args = {'button': button, 'form': form}
    return render(request, 'Testing/display_table.html', args)

def search(request):
    login_checker = LoginCheck('Login', 'valid')
    if login_checker.check_login():
        search= Search()
        args = {'Search': search}
        return render(request, 'Testing/search.html',args)
    else:
        return HttpResponse("<h1>No Login</h1>")


def noaccess(request):

    return HttpResponse("<h1>No Login</h1>")


def check_entry_exist(ref_no):
    database = boto3.resource('dynamodb', region_name='ap-southeast-2', aws_access_key_id=access_key_id_global,
                                  aws_secret_access_key=secret_access_key_global)
    table = database.Table('ME_CFS_DB')
    response = table.query(
            KeyConditionExpression=Key('Reference_No').eq(ref_no)
        )
    if response['Items']:
        return True
    else:
        return False

def write_to_db(ref_no, date_time):
    # Read from DB to see if it exist, if it does do not create a new one.
    database = boto3.resource('dynamodb', region_name='ap-southeast-2', aws_access_key_id=access_key_id_global,
                              aws_secret_access_key=secret_access_key_global)
    table = database.Table('ME_CFS_DB')

    response = table.put_item(
       Item={
                'Reference_No': ref_no,
                'Date_Time': int(date_time),
            }
    )


def update_db(name, value, ref_no, collected_date_time):
    # check existing or not
    # update the existing record

    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2', aws_access_key_id=access_key_id_global,
                               aws_secret_access_key=secret_access_key_global)
    table = dynamodb.Table('ME_CFS_DB')
    Expression_string="set "+name+ "= :r";
    response = table.update_item(
         Key={
              'Reference_No': ref_no,
              'Date_Time': int(collected_date_time),
            },
         UpdateExpression=Expression_string,
         ExpressionAttributeValues={
            ':r': value,
         },
         ReturnValues="UPDATED_NEW"
    )

def update_Login_db(value):
    # check existing or not
    # update the existing record

    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2', aws_access_key_id=access_key_id_global,
                               aws_secret_access_key=secret_access_key_global)
    table = dynamodb.Table('security')
    Expression_string="set Password = :r";
    response = table.update_item(
         Key={
              'Username': 'Login',
            },
         UpdateExpression=Expression_string,
         ExpressionAttributeValues={
            ':r': value,
         },
         ReturnValues="UPDATED_NEW"
    )

def upload_to_db(dictionary):
    print("This is to be uploaded, ", dictionary)
    boolean_val = check_entry_exist(dictionary['Reference_No'])
    print("if that entry already exist:", boolean_val)
    if (boolean_val):
        print("Update it")
        # update it only
        for val in dictionary:
            if (val != 'Reference_No' and val != 'Date_Time' and val != 'upload_to_DB' and val != 'csrfmiddlewaretoken' and val!= 'File_name'):
                print("Resuld_dict:", val, " value:", dictionary[val])
                val1 = val.replace('.', '_')
                update_db(val1, dictionary[val], dictionary['Reference_No'],
                                                  dictionary['Date_Time'])

    else:
        print("Create it")
        # create it and update it
        write_to_db(dictionary['Reference_No'], dictionary['Date_Time'])
        for val in dictionary:
            if (val != 'Reference_No' and val != 'Date_Time' and val != 'upload_to_DB' and val != 'csrfmiddlewaretoken' and val!= 'File_name'):
                print("Resuld_dict:", val, " value:", dictionary[val])
                val1 = val.replace('.', '_')
                update_db(val1, dictionary[val], dictionary['Reference_No'],
                                                  dictionary['Date_Time'])