from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product

class MarketViewsTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(title="test_prod")
        self.user = User.objects.create_user(username='testuser', password='password')
        self.superuser = User.objects.create_superuser(username='superuser', password='password')
        
    def test_product_detail_view(self):
        response = self.client.get(reverse('market:product_detail', kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/products_detail.html')

    def test_create_product_view_without_login(self):
        response = self.client.get(reverse('market:create_product'))
        self.assertNotEqual(response.status_code, 200)

    def test_create_product_view_with_login_but_not_superuser(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('market:create_product'))
        self.assertEqual(response.status_code, 302) 

    def test_create_product_view_with_superuser_login(self):
        self.client.login(username='superuser', password='password')
        response = self.client.get(reverse('market:create_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/products_create.html')
