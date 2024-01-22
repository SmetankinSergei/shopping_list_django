from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from shopping_list.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'shopping_list/category_list.html'
    extra_context = {
        'title': 'all products',
        'is_all_categories': True,
        'products': Product.objects.all(),
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'product',
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'details', 'category', 'img', 'price']
    success_url = reverse_lazy('shopping_list:product_list')
    extra_context = {
        'title': 'create product',
        'is_new_product': True,
    }


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopping_list:product_list')

# def all_products(request):
#     context = {'title': 'all products',
#                'is_all_categories': True,
#                'products': Product.objects.all()}
#     return render(request, 'shopping_list/category_list.html', context)


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        category = Category.objects.get(pk=pk)
        context['category'] = category
        context['title'] = category.name
        context['products'] = Product.objects.filter(category=pk)
        return context


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('shopping_list:product_list')
    extra_context = {
        'title': 'create category',
        'is_new_category': True,
    }


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('shopping_list:product_list')
