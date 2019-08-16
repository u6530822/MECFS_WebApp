from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('display', views.display,name='display'),
    path('displayhtml', views.displayhtml,name='displayhtml'),
    path('post_new', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('details', views.post_detail, name='post_detail'),

]