from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Post

# Create your views here.


### 전체 메인 페이지 ###
def main(req):
    return render(req, 'index.html')


### 게시글들의 제목과 작성자가 쭈욱 나와있는 main페이지 ###


def board_main(req):
    posts = Post.objects
    return render(req, 'board_main.html', {'posts': posts})

### 글의 상세 내용을 볼 수 있는 detail 페이지 ###


def board_detail(req, post_id):
    blog_detail = get_object_or_404(Post, pk=post_id)
    return render(req, 'board_detail.html', {'post': blog_detail})

### 글쓰기 창을 띄우는 페이지 ###

def board_new(req):
    return render(req, 'board_new.html')

### 새 글을 db에 저장하는 함수 ###

def board_create(req):
    post = Post()
    post.title = req.GET['title']
    post.text = req.GET['text']
    post.genre = req.GET['genre']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect("/board/"+str(post.id))

### 글을 삭제하는 함수 ###

def board_delete(req, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("/board/")

def board_edit(req, post_id):
    blog_previous = get_object_or_404(Post, pk=post_id)
    return render(req, "board_edit.html", {'post':blog_previous})

### 글을 수정한 후 db에 저장하는 함수. ###
@csrf_exempt
def board_update(req, post_id):
    post = Post.objects.get(pk=post_id)
    if req.method == 'POST':
        post.title = req.POST.get('title', '')
        post.text = req.POST.get('text', '')
        post.genre = req.POST.get('genre', '')
        post.save()
        return redirect(f"/board/{post.id}")

    return render(req, "board_main.html")
