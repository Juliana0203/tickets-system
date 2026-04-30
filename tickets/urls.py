from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('mis-tickets/', views.mis_tickets, name='mis_tickets'),
    path('ticket/crear/', views.crear_ticket, name='crear_ticket'),
    path('mis-tickets/<int:id_ticket>/', views.detalle_ticket, name='detalle_ticket'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
]