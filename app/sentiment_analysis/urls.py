from django.urls import path, re_path

from .views import audio_recorder, sentiment_analysis, audio_delete

app_name = 'sentiment_analysis'

urlpatterns = [
    path('record/', audio_recorder, name = 'audio_recorder'),
    #path('audio_analyze/', audio_recorder, name = 'audio_recorder'),
    re_path(r'^audio_analyze/$', sentiment_analysis, name='audio_analyze'),
    re_path(r'^audio_delete/$', audio_delete, name='audio_delete'),
]