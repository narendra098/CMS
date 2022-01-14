from django.urls import path, re_path
from . import views

urlpatterns = [

    path('report/', views.report, name='report'),
    path('post/',views.post,name='post' ),

]