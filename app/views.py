from django.shortcuts import render
from rest_framework import viewsets
from .models import Produit
from .serializers import ProduitSerializer
from .models import Categorie

def accueil(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'accueil.html', {
        'produits': produits,
        'categories': categories
    })


class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()  # Récupère tous les produits
    serializer_class = ProduitSerializer  # Utilise le serializer créé

def login(request):
    context = {}
    return render(request, 'login.html', context)
