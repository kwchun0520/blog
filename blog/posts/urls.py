from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("new-post/", views.post_new, name="new-post"),
    path("<slug:slug>", views.post_page, name="page")  ## can also use dynamic urls  post/<id>  ## by default Django capture input as string, <int:id> will capture integer values only
]