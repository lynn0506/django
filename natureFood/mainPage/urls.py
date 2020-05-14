from django.urls import path 
from mainPage import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('question/<int:id>/', views.show_question, name="show"),
    path('question/new/', views.new_question, name="new"),
]