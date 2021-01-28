from django.urls import path

from . import views

# Required to differ paths from different apps
app_name = 'polls'

#all paths that call the view methods
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('vote/<int:question_id>/', views.vote, name='vote'),
]