"""Myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')), #make sure this url comes before shop url
    # path('rosetta/', include('rosetta.urls')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('', include('shoprite.urls', namespace='shoprite')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('account/', include('account.urls', namespace='account')),
]

admin.site.site_header = 'Shoprite Admin'
admin.site.title_header = 'Shoprite Admin Portal'
admin.site.index_title = 'Shoprite Admin Portal'

#this settings was made to serve images from the development server
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)