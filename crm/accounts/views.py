from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

# Create your views here.
def home(request):
    orders = Order.objects.all().order_by('-date_created')
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()
    orders_out_for_delivery = orders.filter(status="Out for delivery").count()
    
    data = {
        'orders': orders[:5], 
        'customers': customers,
        'total_orders': total_orders, 
        'total_customers': total_customers,
        'orders_pending': orders_pending,
        'orders_delivered': orders_delivered,
        'orders_out_for_delivery': orders_out_for_delivery,
    }

    return render(request,'accounts/dashboard.html', { 'data': data })

def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html', { 'products': products })

def customers(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    orders_count = orders.count()
    
    filter = OrderFilter(request.GET, queryset=orders)
    orders = filter.qs

    data = { 
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
        'filter': filter,
        }
    
    return render(request,'accounts/customer.html', data)

def create_order(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=id)
    formset = OrderFormSet(instance= customer, queryset=Order.objects.none())
    # form = OrderForm(initial={ 'customer': customer })
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/') 

    data = { 'formset': formset }
    return render(request, 'accounts/forms/order_form.html', data)

def update_order(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/') 

    data = { 'form': form }
    return render(request, 'accounts/forms/order_form.html', data)

def delete_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/') 

    data = { 'order': order }
    return render(request, 'accounts/forms/delete.html', data)
