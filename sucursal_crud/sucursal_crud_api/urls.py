from django.urls import path
from sucursal_crud_api import views

urlpatterns = [
    path('hello/', views.HelloApiView.as_view())
]