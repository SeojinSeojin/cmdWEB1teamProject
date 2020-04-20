from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
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


def board_delete(req, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("/board/")

### 글을 수정한 후 db에 저장하는 함수. ###
# def board_modify(req, 지금로그인한아이디):
