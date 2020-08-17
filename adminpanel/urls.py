from django.urls import path,include
from . import views
from django.conf.urls.static import static 
from django.conf import settings 


urlpatterns = [

    path('create/',views.create,name='create'),
    path('success', views.success, name = 'success'), 
    path('delete/<str:pk>/', views.delete, name = 'delete'), 
    path('update/<str:pk>/', views.update, name = 'update'), 
    path('', views.stock, name = 'stock'), 

]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)