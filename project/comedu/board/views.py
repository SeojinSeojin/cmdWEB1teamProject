from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

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
# def board_create(req):

### 글을 수정한 후 db에 저장하는 함수. 권한 관련된 문제라 나중에 손 댈 것! ###
# def board_modify(req, 지금로그인한아이디):
