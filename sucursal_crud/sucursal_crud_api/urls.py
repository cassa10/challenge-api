from django.urls import path
from sucursal_crud_api import views

urlpatterns = [
    #path('hello/', views.HelloApiView.as_view()),
    #path('sucursal/', views.SucursalApiView.as_view()),
    #path('sucursal/info/<int:id>/', views.SucursalInfoApiView.as_view()),
    path('', views.HelloApiView.as_view()),
    path('sucursal/<int:id>/', views.SucursalAPIView.as_view()),
    path('sucursal/', views.SucursalAPIView.as_view()),
    path('puntoDeRetiro/<int:id>/', views.PuntoDeRetiroAPIView.as_view()),
    path('puntoDeRetiro/', views.PuntoDeRetiroAPIView.as_view()),
    #GenericAPIView
]