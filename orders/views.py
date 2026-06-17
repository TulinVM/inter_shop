# views.py
# Теперь вместо обычной функции используем CreateView.

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db import transaction
from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Basket
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Создание заказа
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('orders:success')

    def dispatch(self, request, *args, **kwargs):
        self.baskets = Basket.objects.filter(
            user=request.user
        )

        if not self.baskets.exists():
            return redirect('products:index')

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def form_valid(self, form):

        with transaction.atomic():

            form.instance.user = self.request.user

            form.instance.status = Order.STATUS_NEW

            response = super().form_valid(form)

            for basket in self.baskets:

                OrderItem.objects.create(

                    order=self.object,

                    product=basket.product,

                    quantity=basket.quantity,

                    price=basket.product.price

                )

            self.baskets.delete()

        return response

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['baskets'] = self.baskets

        return context
    
    # Просмотр заказа
from django.views.generic import DetailView


class OrderDetailView(DetailView):

    model = Order

    template_name = 'orders/order_detail.html'

    pk_url_kwarg = 'order_id'

    context_object_name = 'order'

    def get_queryset(self):

        return (
            Order.objects
            .for_user(self.request.user)
            .with_items()
        )
    
    # Список заказов
from django.views.generic import ListView


class UserOrdersView(ListView):

    model = Order

    template_name = 'orders/orders.html'

    context_object_name = 'orders'

    paginate_by = 10

    def get_queryset(self):

        qs = (
            Order.objects
            .for_user(self.request.user)
            .with_items()
            .order_by('-created')
        )

        status = self.request.GET.get('status')

        if status:

            qs = qs.filter(status=status)

        return qs
    
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

@login_required
def order_create(request):
    baskets = Basket.objects.filter(user=request.user)

    if not baskets.exists():
        return redirect('products:index')

    if request.method == 'POST':

        name = request.POST.get('name')
        address = request.POST.get('address')
        # status = request.POST.get('status')
        phone = request.POST.get('phone')

        with transaction.atomic():

         order = Order.objects.create(
             user=request.user,
             customer_name=name,
             address=address,
             status=Order.STATUS_NEW,
             phone =phone,

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
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(request, 'orders/order_detail.html', {
        'order': order,
    })   