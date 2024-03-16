from django.urls import path

from order import views

urlpatterns = [
    path('address/', views.AddressListCreateAPI.as_view()),
    path('address/<int:pk>/', views.AddressAPI.as_view()),

    path('order/', views.OrderCreateAPI.as_view()),
    path('order/<int:pk>/', views.OrderAPI.as_view()),
]
