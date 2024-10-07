from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from typing import Union
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

def post_list(request:HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-date")
    return render(request=request, template_name="posts/post_list.html", context={"posts":posts, "username": "User"}) ## for django to locate the template with same name


def post_page(request:HttpRequest, slug:str) -> Union[HttpResponse, HttpResponseNotFound]:
    post = Post.objects.get(slug=slug)
    return render(request=request, template_name="posts/post_page.html", context={"post":post})


# def redirect(request:HttpRequest, slug:str) -> HttpResponseRedirect:
#     url = reverse("post", args=[slug])
#     return HttpResponseRedirect(redirect_to=url)


@login_required(login_url="users:login")
def post_new(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("posts:list")
    form = forms.CreatePost()
    return render(request=request, template_name="posts/post_new.html", context={"form":form})