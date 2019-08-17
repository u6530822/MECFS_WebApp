from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('display', views.display,name='display'),
    path('displayhtml', views.displayhtml,name='displayhtml'),
    path('post_new', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    path('new',views.upload_file,name='upload_file'),



]