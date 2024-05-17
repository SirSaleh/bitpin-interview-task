from braces import views as braces_views
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "market/products_list.html"


class ProductDetail(TemplateView):
    template_name = "market/products_detail.html"


class CreateProduct(braces_views.LoginRequiredMixin,
                    braces_views.SuperuserRequiredMixin,
                    TemplateView):
    template_name = 'market/products_create.html'
