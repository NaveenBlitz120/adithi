from django.urls import path,include
from . import views
from django.conf.urls.static import static 
from django.conf import settings 


urlpatterns = [

    path('', views.home, name = 'home'),
    path('products', views.stock, name = 'products'),   
    path('flowers', views.stockflo, name = 'floproducts'),   
    path('create/',views.create,name='create'),
    path('delete/<str:pk>/', views.delete, name = 'delete'), 
    path('update/<str:pk>/', views.update, name = 'update'),    
    path('updateflo/<str:pk>/', views.updateflo, name = 'updateflo'),    
    path('deleteflo/<str:pk>/', views.deleteflo, name = 'deleteflo'),    
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name="logout"),
    path('updateorder/<str:pk>/', views.update_order, name = 'updateorder'), 
    path('updateoffer/', views.update_offer, name = 'updateoffer'), 
    path('view/<str:pk>/', views.view, name = 'view'), 
    path('geo/', views.geo, name = 'geo'), 

    


]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)