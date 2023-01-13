from django.urls import path
from posts import views 

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('<int:id>/', views.post_detials, name = 'post_detials'),
]