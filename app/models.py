from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/', default='produits/default.png')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
