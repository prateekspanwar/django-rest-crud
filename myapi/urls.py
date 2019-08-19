from django.urls import path, include # new
from rest_framework.authtoken.views import obtain_auth_token
from myapi.core import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
    path('inventory/<int:pk>', views.InventoryView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('books/', include('books.urls')),

    
]
