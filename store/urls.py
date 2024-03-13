from django.urls import path

from store import views

urlpatterns = [
    path('product/', views.ProductListAPI.as_view()),
    path('product/<int:pk>/', views.ProductDetailAPI.as_view()),
    path('cart/', views.CartAPI.as_view()),
]
