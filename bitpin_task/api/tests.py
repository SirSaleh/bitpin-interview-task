from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from market.models import Product


class ProductEndpointsTest(APITestCase):
    
    def setUp(self):
        self.logged_user_1 = APIClient()
        self.product = Product.objects.create(title="test_bitpin_product")
        self.product_2 = Product.objects.create(title="test_bitpin_product 2")

        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword', is_superuser=False)
        self.superuser = User.objects.create_superuser(username='superuser', 
                                                       password='superpassword')
        super().setUp()
    
    def test_retrieve_products(self):
        response = self.client.get(reverse('api:product-detail',
                                           kwargs={"pk": self.product.id}),
                                           format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "test_bitpin_product")

    def test_list_products(self):
        response = self.client.get(reverse('api:product-list'), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['count'], 2)

    def test_create_products(self):
        # anonymous clinet
        response = self.client.post(reverse('api:product-list'),
                                    data={'title': 'new_product'}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # user clinet
        self.client.force_login(self.user)
        response = self.client.post(reverse('api:product-list'),
                                    data={'title': "new_product"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # admin client
        self.client.force_login(self.superuser)
        response = self.client.post(reverse('api:product-list'),
                                    data={'title': "new_product"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "new_product")

    def test_patch_products(self):
        # anonymous user
        response = self.client.patch(reverse('api:product-detail',
                                             kwargs={"pk": self.product.id}),
                                             data={'title': 'new_title_for_default_product'},
                                             format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # ordinary client
        self.client.force_login(self.user)
        response = self.client.patch(reverse('api:product-list'),
                                    data={'title': "new_product"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # superuser
        self.client.force_login(self.superuser)
        response = self.client.patch(reverse('api:product-detail',
                                             kwargs={'pk': self.product.id}),
                             data={'title': "new_title_for_default_product"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "new_title_for_default_product")
    
    def test_delete_products(self):
        # at first there is {product_count_before} products
        response = self.client.get(reverse('api:product-list'), format="json")

        product_count_before = response.data['count']

        # we delete one with anonymous user
        response = self.client.delete(reverse('api:product-detail',
                                             kwargs={'pk': self.product.id}),
                                             format="json")
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # we delete one with normal user
        self.client.force_login(self.user)
        response = self.client.delete(reverse('api:product-detail',
                                             kwargs={'pk': self.product.id}),
                                             format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # we delete with superuser
        self.client.force_login(self.superuser)
        response = self.client.delete(reverse('api:product-detail',
                                             kwargs={'pk': self.product.id}),
                                             format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Now there shoul be {product_count-1} remaining
        response = self.client.get(reverse('api:product-list'), format="json")

        product_count_after = response.data['count']
        self.assertEqual(product_count_after, product_count_before-1)



        
