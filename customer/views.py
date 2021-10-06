from django.db.models import Q
from django.shortcuts import render
from django.views import View

# Create your views here.
from customer.models import MenuItem, OrderModel


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        drinks = MenuItem.objects.filter(category__name__contains='Drinks')
        dessert = MenuItem.objects.filter(category__name__contains='Dessert')
        starter = MenuItem.objects.filter(category__name__contains='Starter')
        special = MenuItem.objects.filter(category__name__contains='special')
        breakfast = MenuItem.objects.filter(category__name__contains='Breakfast')
        beverages = MenuItem.objects.filter(category__name__contains='Beverages')
        # pass to context
        context = {
            'starter': starter,
            "drinks": drinks,
            'dessert': dessert,
            'special': special,
            'breakfast': breakfast,
            "beverages": beverages,
        }
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
        return render(request, 'customer/order_conf.html', context)
        messeges.


class Search(View):

    def search(self, request, *args, **kwargs):
        search = MenuItem.objects.get(
            Q(name__startswith=['Tea', 'Chipo', ])
        )
        context = {
            'search': search
        }
        return render(request, 'customer/order.html', context)
