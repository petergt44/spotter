from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('route/<str:start>/<str:end>/', views.get_route),
    path('admin/', admin.site.urls),

    path('', views.get_route, name='get_route'),
]