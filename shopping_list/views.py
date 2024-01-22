from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from shopping_list.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'shopping_list/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sorting = self.request.GET.get('sorting', 'by_date')
        context['sorting'] = sorting
        context['title'] = 'all products'
        context['is_all_categories'] = True
        products = Product.objects.all()
        if sorting == 'by_date':
            context['products'] = products.order_by('change_at')
        elif sorting == 'by_price':
            context['products'] = products.order_by('price')
        return context


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


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'details', 'category', 'img', 'price']
    success_url = reverse_lazy('shopping_list:product_list')
    extra_context = {
        'title': 'update product',
    }


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopping_list:product_list')
    extra_context = {'title': 'delete product'}


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        sorting = self.request.GET.get('sorting', 'by_date')
        context['sorting'] = sorting
        category = Category.objects.get(pk=pk)
        context['category'] = category
        context['title'] = category.name
        products = Product.objects.filter(category=pk)
        if sorting == 'by_date':
            context['products'] = products.order_by('change_at')
        elif sorting == 'by_price':
            context['products'] = products.order_by('price')
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
    extra_context = {'title': 'delete category'}
