from django.urls import path
from . import views

app_name = 'shoprite'

urlpatterns = [
	path('', views.index, name='index'),
	path('shop/', views.shop, name='shop'),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
	path('contact/', views.contact, name='contact'),
	path('profile/', views.profile, name='profile'),
	path('portfolio/', views.portfolio, name='portfolio'),
	
]