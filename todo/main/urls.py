from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('archive/', views.archive, name='archive'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/done', views.done, name='todo_done')
]