from django.urls import path
from . import views
from .views import SendMessageView

urlpatterns = [
    path('',views.home, name='home'),
    path('chat/',views.chat, name='chat'),
    path('resources/',views.resources, name='resources'),
    path('tutorials/',views.tutorials, name='tutorials'),
    path('about/',views.about, name='about'),
    path('send_message/', SendMessageView.as_view(), name='send_message'),
]

