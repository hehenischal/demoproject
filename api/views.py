from django.shortcuts import render
from django.http import JsonResponse
from home.models import Article
from .serializers import ArticleSerializer

def index(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    message = {
        'message': 'Welcome to the API home page',
        'status': 'success',
        'code': 200,
        'articles': serializer.data
    }
    
    return JsonResponse(message, safe=False)

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@require_POST
@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = request.POST
        article = Article.objects.create(
            title=data.get('title'),
            content=data.get('content'),
        )
        serializer = ArticleSerializer(article)
        message = {
            'message':'successfully created',
            'status':'success',
            'code':201,
            'data': serializer.data
        }
        return JsonResponse(message, safe=False)


def detail(request, slug):
    object = Article.objects.filter(slug=slug).first()
    serializer = ArticleSerializer(object)
    return JsonResponse(serializer.data, safe=False)


def delete(request, slug):
    return JsonResponse({'message': f'Delete endpoint for {slug}'})