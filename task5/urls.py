from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('sign_up_by_django/', views.sign_up_by_django, name='sign_up_by_django'),
    path('sign_up_by_html/', views.sign_up_by_html, name='sign_up_by_html'),
]

