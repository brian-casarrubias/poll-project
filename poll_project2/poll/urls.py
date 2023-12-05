from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('poll/<int:pk>/', views.pollstart, name='poll-page'),
    path('results-page/', views.results, name='results-page'),
    path('create-poll/', views.ChoiceCreateView.as_view(), name='poll-create' ),
    path('create-question/', views.QuestionCreateView.as_view(), name='question-create'),
   
]