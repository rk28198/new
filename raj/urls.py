from django.contrib import admin
from django.urls import path
from raj import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('about',views.about, name='about'),
    path('Education',views.Education, name='Education'),
    path('contact',views.contact, name='contact'),
    path('form',views.form, name='form'),
    path('Mission',views.Mission, name='Mission'),
    path('aboutscho',views.aboutscho, name='aboutscho'),
    path('child',views.child, name='child'),
    path('goal',views.goal, name='goal'),
    path('health',views.health, name='health'),
    path('team',views.team, name='team'),
    path('vision',views.vision, name='vision'),
    path('Womens',views.Womens, name='Womens'),
    path('nav',views.nav, name='nav'),
    path('uploadfile',views.uploadfile, name='uploadfile'),
    path('more',views.more, name='more'),
    path('schobase',views.schobase, name='schobase'),
    path('eligibi',views.eligibi, name='eligibi'),
    path('syllbus',views.syllbus, name='syllbus'),
    path('hindi',views.hindi, name='hindi'),
    path('hindig',views.hindig, name='hindig'),
    path('formhindi',views.formhindi, name='formhindi'),
    path('Exam',views.Exam, name='Exam'),
]