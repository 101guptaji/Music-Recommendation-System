from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('review/', views.review_list, name='review_list'),
    path('', views.song_list, name='song_list'),
    path('reviews/<int:pk>', views.review_detail, name='review_detail'),
    path('Song/', views.song_list, name='song_list'),
    path('Song/<int:pk>', views.song_detail, name='song_detail'),
    path('Song/<int:pk>/add_review', views.add_review, name='add_review'),
    path('accounts/logout/', views.logout_view, name='logout_view'),
    path('accounts/register/', views.SignUp.as_view(), name = 'signup'),

    ]