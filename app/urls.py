from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProduitViewSet

# Crée un routeur et enregistre le viewset
router = DefaultRouter()
router.register(r'produits', ProduitViewSet)

urlpatterns = [
    path('', views.accueil, name='accueil'),  
    path('login/', views.login, name='login'), 
    path('api/', include(router.urls)),  # API des produits
]
