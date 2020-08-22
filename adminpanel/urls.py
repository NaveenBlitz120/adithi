from django.urls import path,include
from . import views
from django.conf.urls.static import static 
from django.conf import settings 


urlpatterns = [

    path('', views.home, name = 'home'),
    path('products', views.stock, name = 'products'), 
    path('create/',views.create,name='create'),
    path('delete/<str:pk>/', views.delete, name = 'delete'), 
    path('update/<str:pk>/', views.update, name = 'update'), 
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name="logout"),
    path('updateorder/<str:pk>/', views.update_order, name = 'updateorder'), 
    path('view/<str:pk>/', views.view, name = 'view'), 

    


]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)