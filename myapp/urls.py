from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # Homepage with login form
    path('round1/', views.round1, name='round1'),
    path('round2/', views.round2, name='round2'),
    path('round3/', views.round3, name='round3'),
    path('round4/', views.round4, name='round4'),
    path('not-selected/', views.not_selected, name='not_selected'),
    path('judges-online/', views.judge_online_login, name='judge_online_login'),
    path('judge-round1/', views.judge_round1, name='judge_round1'),
    path('judge-round2/', views.judge_round2, name='judge_round2'),
    path('judge-round3/', views.judge_round3, name='judge_round3'),
    path('judges-offline/', views.judge_offline_login, name='judge_offline_login'),
    path('offline-judge-round1/', views.offline_judge_round1, name='offline_judge_round1'),
    path('offline-judge-round2/', views.offline_judge_round2, name='offline_judge_round2'),
    path('offline-judge-round3/', views.offline_judge_round3, name='offline_judge_round3'),
    path('round1-upload/', views.round1_upload, name='round1_upload'),
    path('round2-upload/', views.round2_upload, name='round2_upload'),
    path('round3-upload/', views.round3_upload, name='round3_upload'),
    path('success/', views.success_page, name='success_page'),
]
