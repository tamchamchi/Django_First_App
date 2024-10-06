from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hihi", views.hihi, name="hihi"),
    path('<int:post_id>/', views.blog_details, {"extra_info": "Tam Anh", "hello" : 1}, name="post_detail"),
]

