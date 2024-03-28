from django.urls import path
from . import views

urlpatterns = [
        path('', views.home_page, name='home_page'),
        path('news/all/', views.all_news_page, name='all_news_page'),
        path('news/detail/<int:pk>/', views.news_detail_page, name='news_detail_page'),
        path('user/sign-up/', views.sign_up_page, name = 'sign_up_page'),
        path('user/login/', views.login_page, name='login_page'),
        path('user/logout/', views.logout_request, name='logout_request'),
]