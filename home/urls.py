from django.urls import path
from .views import index, create, detail, delete

app_name = "articles"
urlpatterns = [
    path('', index, name="home"),
    path('create/', create, name="create"),
    path('detail/<slug:slug>/', detail, name="detail"),
    path('delete/<slug:slug>/', delete, name="delete"),
]
