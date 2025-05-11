from django.contrib import admin
from django.utils.html import format_html
from .models import Categorie, Produit

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'date_ajout', 'image_preview')
    list_filter = ('categorie', 'date_ajout')
    search_fields = ('nom', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return "Aucune image"
    image_preview.short_description = 'Image'
