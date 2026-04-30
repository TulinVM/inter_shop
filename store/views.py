from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        products.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })
        total += product.price * quantity

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total
    })


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')

        cart = request.session.get('cart', {})

        order = Order.objects.create(
            customer_name=name,
            address=address
        )

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        request.session['cart'] = {}

        return render(request, 'store/success.html', {'order': order})

    return render(request, 'store/checkout.html')
