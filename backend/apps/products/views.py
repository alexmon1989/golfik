from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404
from .models import Category, Product


class CategoryListView(ListView):
    """Отображает страницу со списком категорий."""
    queryset = Category.objects.enabled().order_by('-weight')
    template_name = 'products/categories/list.html'


class ProductListView(ListView):
    """Отображает страницу со списком продуктов конкретной категории."""
    template_name = 'products/products/list.html'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.enabled().filter(category__slug=self.kwargs['slug']).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.enabled().filter(slug=self.kwargs['slug']).first()
        if not context['category']:
            raise Http404('Категория не включена.')
        context['categories'] = Category.objects.enabled().order_by('-weight')
        return context


class ProductDetailView(DetailView):
    """Отображает страницу товара."""
    queryset = Product.objects.enabled()
    template_name = 'products/product/detail.html'
