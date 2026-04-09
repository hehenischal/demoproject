from django.shortcuts import render,redirect
from .models import Article
# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def create(req):
    if req.method == "POST":
        title = req.POST.get('title')
        content = req.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        return redirect('articles:home')
    return render(req, 'create.html')


def detail(req,slug):
    context = {
        'article':Article.objects.get(slug=slug)
    }
    return render(req, 'detail.html', context)
def delete(req,slug):
    pass