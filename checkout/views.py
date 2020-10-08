from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51HZbr6FBSfP9XloYNNpmZ0mt7Xd4F0Ulc11uLqYf9AUE6RzB9MUzrtD6tTWRIWQFmmT9x6CloqN6sn73SUzow8xL00uf42xnIp",
        'client_secret': "test client secret",
    }

    return render(request, template, context)