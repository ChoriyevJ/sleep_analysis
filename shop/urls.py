from django.urls import path

from shop import views


urlpatterns = [
    path('product/', views.ProductListAPI.as_view()),
    path('product/<int:pk>/', views.ProductDetailAPI.as_view()),
    # path('product/<int:pk>/add', views.ProductDetailAPI.as_view()),
    path('cart/', views.CartAPI.as_view()),
    path('cart/create/', views.CartCreateAPI.as_view()),
    path('cart/<int:pk>/update/', views.CartUpdateAPI.as_view()),
    path('cart/<int:pk>/destroy/', views.CartDeleteAPI.as_view()),

]
