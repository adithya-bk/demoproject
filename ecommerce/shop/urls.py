"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
app_name='shop'
urlpatterns = [
    path('',views.Home.as_view(),name="category"),
    path('categorydetails/<int:pk>',views.CategoryDetails.as_view(),name="categorydetails"),
    path('productdetails/<int:pk>', views.ProductDetails.as_view(), name="productdetails"),
    path('register', views.register, name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('addcategories',views.AddCategories.as_view(),name="addcategories"),
    path('addproducts',views.AddProducts.as_view(),name="addproducts"),
    path('addstock/<int:pk>',views.AddStock.as_view(),name="addstock"),

]
