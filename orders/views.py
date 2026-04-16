from django.shortcuts import render, redirect
from products.models import Basket
from .models import Order, OrderItem


def order_create(request):
    baskets = Basket.objects.filter(user=request.user)

    if not baskets.exists():
        return redirect('products:index')

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')

        order = Order.objects.create(
            user=request.user,
            customer_name=name,
            address=address
        )

        # перенос корзины в заказ
        for basket in baskets:
            OrderItem.objects.create(
                order=order,
                product=basket.product,
                quantity=basket.quantity,
                price=basket.product.price
            )

        # очистка корзины
        baskets.delete()

        return redirect('orders:success')

    return render(request, 'orders/order-create.html', {
        'baskets': baskets
    })

def success(request):
    return render(request, 'orders/success.html')


def confirmed_orders(request):
    orders = Order.objects.filter(status='confirmed')

    return render(request, 'orders/confirmed_orders.html', {
        'orders': orders
    })