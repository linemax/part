from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.views import View

# Create your views here.
from customer.models import MenuItem, OrderModel, Category


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        categories = Category.objects.all()
        menu_items = MenuItem.objects.all()
        context = {'categories': categories, 'menu_items': menu_items}
        # render
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': [],
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_id = []

        for item in order_items['items']:
            price += item['price']
            item_id.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order_list = OrderModel.objects.all()
        order.items.add(*item_id)

        context = {
            'items': order_items['items'],
            'price': price,
            'orderlist': order_list
        }
        messages.success(request, 'Your order has been submitted successfully')
        return render(request, 'customer/order_conf.html', context)



class Search(View):

    def search(self, request, *args, **kwargs):
        search = MenuItem.objects.get(
            Q(name__startswith=['Tea', 'Chipo', ])
        )
        context = {
            'search': search
        }
        return render(request, 'customer/order.html', context)
