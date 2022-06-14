from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import random

def get_max_price(n_list):
	price_list = [item.price for item in n_list]
	max_p = max(price_list)
	return max_p


page = products = ''

def index(request):
	category = None
	top_list = Product.objects.filter(available=True)
	# top_list = top_list[:10]

	categories = Category.objects.all()
	top_cat = list()
	top_products = list()
	for category in categories:
		# Latest Products handler
		top_item = top_list.filter(category=category)[:1]
		print(top_item)
		top_cat.append(top_item[0])

		# Top New handler
		price_list = top_list.filter(category=category)
		top_price = get_max_price(price_list)
		top_product = price_list.filter(price=top_price)
		top_products.append(top_product[0])

	# To generate 3 random top price item from all categories
	top_new = random.sample(top_products, k=3)
	top_view = random.sample(top_products, k=3)
	top_seller = random.sample(top_products, k=3)

	#Context processor
	context = {
		'top_cat':top_cat,
		'top_new':top_new,
		'top_seller':top_seller,
		'top_view':top_view
	}
	return render(request, 'shoprite/product/index.html', context)



def shop(request):
	category = None
	catalog = dict()
	categories = Category.objects.all()
	all_products = Product.objects.filter(available=True)
	
	# if category_slug:
	# category = get_object_or_404(Category, slug=category_slug)
	for category in categories:
		filter_products = all_products.filter(category=category)[:4]
		# print(filter_products)
		catalog[category]=filter_products
		# print(catalog)
	return render(request, 'shoprite/product/shop.html', {'catalog':catalog, 'categories':categories, 'all_products':all_products})

	#this is the Json part
	#data = {"results":list(all_products.values("name", "created", "price"))}
	#return JsonResponse(data)
	# return render(request, 'shoprite/product/shop.html')


def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	all_products = Product.objects.filter(available=True)
	
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		all_products = all_products.filter(category=category)
		#paginator part added for categorized products
		paginator = Paginator(all_products, 6)	# 9 products per pages
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			# if page is not an integer, deliver the first page
			products = paginator.page(1)
		except EmptyPage:
			# if page is out of range, deliver last page of results
			products = paginator.page(paginator.num_pages)
			#paginator part ends here
	else:
		#paginator part added for all categories
		paginator = Paginator(all_products, 6)	# 9 products per pages
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			# if page is not an integer, deliver the first page
			products = paginator.page(1)
		except EmptyPage:
			# if page is out of range, deliver last page of results
			products = paginator.page(paginator.num_pages)
			#paginator part ends here
	return render(request, 'shoprite/product/category.html', {'category':category, 'categories':categories, 'page':page, 'products':products})

	#this is the Json part
	#data = {"results":list(all_products.values("name", "created", "price"))}
	#return JsonResponse(data)


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	return render(request, 'shoprite/product/detail.html', {'product':product, 'cart_product_form':cart_product_form})

	#the Json part
	#data = {"results":{"name":product.name, "created":product.created, "price":product.price}}
	#return JsonResponse(data)

def contact(request):
	return render(request, 'shoprite/product/contact.html')

def portfolio(request):
	return render(request, 'shoprite/product/portfolio.html')

def profile(request):
	return render(request, 'shoprite/product/profile.html')