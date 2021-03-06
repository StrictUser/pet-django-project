from django.urls import path
from . import views

app_name = 'osint'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:url>/', views.post_category, name='post_category')
]
