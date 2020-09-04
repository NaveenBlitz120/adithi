"""adithi_Ecart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('viewproduct/<str:pk>/', views.viewproduct, name="viewproduct"),
	path('viewflower/<str:pk>/', views.viewflower, name="viewflower"),
	path('vegetables/', views.vegetables, name="vegetables"),
	path('fruits/', views.fruits, name="fruits"),
    path('groceries/', views.groceries, name="groceries"),
    path('nuts/', views.nuts, name="nuts"),
    path('daals/', views.daals, name="daals"),
    path('oils/', views.oils, name="oils"),
    path('homecare/', views.homecare, name="homecare"),
    path('babycare/', views.babycare, name="babycare"),
    path('personalcare/', views.personalcare, name="personalcare"),
    path('beverages/', views.beverages, name="beverages"),
    path('snacks/', views.snacks, name="snacks"),
    path('flowers/', views.flowers, name="flowers"),
    path('bill/', views.htmlbill, name="bill"),
    path('deletecookie/', views.deletecookie, name="deletecookie"),
    path('deletecartcookie/', views.deletecartcookie, name="deletecartcookie"),
]
