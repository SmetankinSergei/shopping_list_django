from django.urls import path

from shopping_list import views

app_name = 'shopping_list'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('create_prod/', views.ProductCreateView.as_view(), name='create_prod'),
    path('update_prod/<int:pk>/', views.ProductUpdateView.as_view(), name='update_prod'),
    path('detail_prod/<int:pk>', views.ProductDetailView.as_view(), name='detail_prod'),
    path('delete_prod/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_prod'),
    path('category_list/<int:pk>', views.CategoryListView.as_view(), name='category_list'),
    path('create_cat/', views.CategoryCreateView.as_view(), name='create_cat'),
    path('delete_cat/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_cat'),
]
