from django.shortcuts import render, redirect
from products.models import Basket
from .models import Order, OrderItem
from django.shortcuts import redirect, get_object_or_404


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
    orders = Order.objects.filter(user=request.user, status='confirmed')

    return render(request, 'orders/confirmed_orders.html', {
        'orders': orders
    })

def confirm_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)

        # меняем статус
        order.status = 'confirmed'
        order.save()

    return redirect('orders:confirmed_orders')
