from django.urls import path
from . import views
from .views import SendMessageView

urlpatterns = [
    path('',views.home, name='home'),
    path('chat/',views.chat, name='chat'),
    path('send_message/', SendMessageView.as_view(), name='send_message'),
]

