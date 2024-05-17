from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "market/products_list.html"


class ProductDetail(TemplateView):
    template_name = "market/products_detail.html"