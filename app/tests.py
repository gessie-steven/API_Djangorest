from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Produit, Categorie

class ProduitAPITestCase(APITestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Informatique")
        
        self.image = SimpleUploadedFile(
            name='test.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )

        self.produit = Produit.objects.create(
            nom="Ordinateur portable",
            description="Un ordinateur puissant",
            prix=999.99,
            image=self.image,
            categorie=self.categorie
        )

        self.list_url = reverse('produit-list')
        self.detail_url = reverse('produit-detail', args=[self.produit.id])

    def test_liste_produits(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_creation_produit(self):
        image_file = SimpleUploadedFile(
            name='souris.jpg',
            content=b'image-data',
            content_type='image/jpeg'
        )
        data = {
            "nom": "Souris Gamer",
            "description": "Souris RGB haute précision",
            "prix": "49.99",  
            "image": image_file,
            "categorie": self.categorie.id
        }
        response = self.client.post(self.list_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produit.objects.count(), 2)

    def test_detail_produit(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nom"], self.produit.nom)

    def test_modification_produit(self):
        new_image = SimpleUploadedFile(
            name='new_image.jpg',
            content=b'new-image-data',
            content_type='image/jpeg'
        )
        data = {
            "nom": "Ordinateur modifié",
            "description": self.produit.description,
            "prix": str(self.produit.prix),
            "image": new_image,
            "categorie": self.categorie.id
        }
        response = self.client.put(self.detail_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.produit.refresh_from_db()
        self.assertEqual(self.produit.nom, "Ordinateur modifié")

    def test_suppression_produit(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produit.objects.count(), 0)
