from django.shortcuts import render
from products.models import Basket
from .models import Order, OrderItem
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Order.objects.filter(user=request.user)
from phonenumber_field.modelfields import PhoneNumberField

@login_required
def order_create(request):
    baskets = Basket.objects.filter(user=request.user)

    if not baskets.exists():
        return redirect('products:index')

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        # status = request.POST.get('status')
        # phone = request.POST.get('phone')

        order = Order.objects.create(
            user=request.user,
            customer_name=name,
            address=address,
            status='confirmed',
            # phone = 'phone',


        #     widgets = {
        #    'status': forms.order_status(attrs={'type': 'STATUS_CHOICES'}),
        # }
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

@login_required
def success(request):
    return render(request, 'orders/success.html')

@login_required
def confirmed_orders(request):
    orders = Order.objects.filter(user=request.user, status='confirmed')

    return render(request, 'orders/confirmed_orders.html', {
        'orders': orders
    })

@login_required
def confirm_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id, user=request.user)
     
        # меняем статус
        order.status = 'confirmed'
        order.save()

    return redirect('orders:confirmed_orders')
###
@login_required
def profile(request):
    return render(request, 'orders/profile.html')

@login_required
def user_orders(request):
    status = request.GET.get('status')

    orders = Order.objects.filter(user=request.user).order_by('-created')

    if status:
        orders = orders.filter(status=status)

    return render(request, 'orders/orders.html', {
        'orders': orders
    })

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    return render(request, 'orders/order_detail.html', {
        'order': order
    })
#########
@login_required
def order_status(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
       
        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )

        # переключение статуса
        if order.status == Order.STATUS_NEW:
            order.status = Order.STATUS_CONFIRMED

        elif order.status == Order.STATUS_CONFIRMED:
            order.status = Order.STATUS_SHIPPED
            
        elif order.status == Order.STATUS_SHIPPED:
            order.status = Order.STATUS_NEW

        order.save()
       
    return redirect(request.META.get('HTTP_REFERER', 'orders:user_orders'))


# # Получаем выбранное значение фильтра
#         selected_asu = self.request.GET.get('name_asu')
#         print("Выбранное АСУ:", selected_asu)  # Вывод в консоль
#        # messages.info(self.request, f"Вы выбрали АСУ: {selected_asu}")  # Вывод в браузере

#         selected_uso = self.request.GET.get('name_uso')
#         print("Выбранное УСО:", selected_uso)  # Вывод в консоль
#         # messages.info(self.request, f"Вы выбрали УСО: {selected_uso}")  # Вывод в браузере

