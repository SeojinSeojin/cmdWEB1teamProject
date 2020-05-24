from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Wiki

# Create your views here.

### 위키의 제목과 최근 업데이트 날짜가 쭈욱 나와있는 main페이지 ###


def wiki_main(req):
    wiki = Wiki.objects
    return render(req, 'wiki_main.html', {'wiki': wiki})

### 글의 상세 내용을 볼 수 있는 detail 페이지 ###


def wiki_detail(req, wiki_id):
    blog_detail = get_object_or_404(Wiki, pk=wiki_id)
    return render(req, 'wiki_detail.html', {'wiki': blog_detail})

### 글쓰기 창을 띄우는 페이지 ###


def wiki_new(req):
    return render(req, 'wiki_new.html')

### 새 글을 db에 저장하는 함수 ###


def wiki_create(req):
    wiki = Wiki()
    wiki.title = req.GET['title']
    wiki.text = req.GET['text']
    wiki.update_date = timezone.datetime.now()
    wiki.writer = req.user
    wiki.save()
    return redirect("/wiki/"+str(wiki.id))

### 글을 삭제하는 함수 ###


def wiki_delete(req, wiki_id):
    wiki = Wiki.objects.get(id=wiki_id)
    wiki.delete()
    return redirect("/wiki/")


def wiki_edit(req, wiki_id):
    wiki_previous = get_object_or_404(Wiki, pk=wiki_id)
    return render(req, "wiki_edit.html", {'wiki': wiki_previous})

### 글을 수정한 후 db에 저장하는 함수. ###
@csrf_exempt
def wiki_update(req, wiki_id):
    wiki = Wiki.objects.get(pk=wiki_id)
    if req.method == 'POST':
        wiki.text = req.POST.get('text', '')
        wiki.save()
        return redirect(f"/wiki/{wiki.id}")

    return render(req, "wiki_main.html")
