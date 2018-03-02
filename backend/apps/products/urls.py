from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name="categories_list"),
    path('<slug:slug>/', ProductListView.as_view(), name="products_list"),
    path('<slug:category_slug>/<int:pk>-<slug:slug>/', ProductDetailView.as_view(), name="product_detail"),
]
