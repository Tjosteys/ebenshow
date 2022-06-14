import braintree
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

# Create your views here.
braintree.Configuration.configure(
	braintree.Environment.Sandbox, 
	merchant_id = settings.BRAINTREE_MERCHANT_ID, 
	public_key = settings.BRAINTREE_PUBLIC_KEY, 
	private_key = settings.BRAINTREE_PRIVATE_KEY
)

def payment_process(request):
	order_id = request.session.get('order_id')
	order = get_object_or_404(Order, id=order_id)

	if request.method == 'POST':
		#retrieve nonce
		nonce = request.POST.get('payment_method_nonce', None)
		#create and submit transaction
		result = braintree.Transaction.sale({'amount':'{:.2f}'.format(order.get_total_cost()), 'payment_method_nonce':nonce, 'options':{'submit_for_settlement':True}})
		if result.is_success:
			#mark the order as paid
			order.paid = True
			#store the unique transaction id
			order.braintree_id = result.transaction.id
			order.save()
			return redirect('payment:done')
		else:
			return redirect('payment:canceled')
	else:
		#generate token
		client_token = braintree.ClientToken.generate()
		return render(request, 'payment/process.html', {'order':order, 'client_token':client_token})


def payment_done(request):
	return render(request, 'payment/done.html')

def payment_canceled(request):
	return render(request, 'payment/canceled.html')