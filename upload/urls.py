from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('display', views.display,name='display'),
    path('displayhtml', views.displayhtml,name='displayhtml'),
    path('post_new', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('new',views.upload_file,name='upload_file'),
    path('results/',views.post_results,name='post_results'),
    path('post/<pk>/remove/',views.post_remove,name='post_remove'),
    path('upload_DB',views.upload_DB,name='upload_DB'),
    path('login', views.login, name='login'),

]