from __future__ import absolute_import, unicode_literals
# from celery.decorators import task
from django.core.mail import send_mail
from .models import Order

# @task
def order_created(order_id):
	"""
		Task to send an e-mail notification when order is succesfully created.
	"""

	order = Order.objects.get(id=order_id)
	subject = 'Order nr. {}'.format(order.id)
	message = 'Dear {}, \n\nYou have succesfully placed an order. Your order id is {}'.format(order.first_name, order.id)
	mail_sent = send_mail(subject, message, 'admin@shoprite.com', [order.email])
	return mail_sent