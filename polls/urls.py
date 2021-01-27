from django.urls import path

from . import views

# Required to differ paths from different apps
app_name = 'polls'

#all paths that call the view methods
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:question_id>/', views.detail, name='detail'),
    path('vote/<int:question_id>/', views.vote, name='vote'),
    path('result/<int:question_id>/', views.result, name='result')
]