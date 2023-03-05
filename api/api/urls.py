from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', views.index, name='index'),
    path('polls/', views.PollListView.as_view(), name='poll_list', ),
    path('polls/create/', views.PollCreateView.as_view(), name='poll_create'),
    path('polls/<int:pk>/', views.PollDetailView.as_view(), name='poll_detail'),
    path('polls/<int:pk>/update/', views.PollUpdateView.as_view(), name='poll_update'),
    path('polls/<int:pk>/delete/', views.PollDeleteView.as_view(), name='poll_delete'),
    path('polls/<int:pk>/vote/', views.vote, name='vote'),
]
