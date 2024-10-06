from django.shortcuts import render
from django.http import HttpResponse
from django.utils.archive import extract


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hihi(request):
    return HttpResponse("Hello, world. You're at the polls hihi.")

def blog_details(request, post_id, **kwargs):
    extra_info1 = kwargs.get('hello', "None")
    extra_info2 = kwargs.get('extra_info', "None")
    return HttpResponse(f"""
    This is blog post {post_id} with extra info: {extra_info1} </br>
    This is blog post {post_id} with extra info: {extra_info2}
    """)
