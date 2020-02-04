from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from shop.models import Product
from .models import Wishlist
from django.contrib.auth.decorators import login_required

# Create your views here.

def wishlist(request):
	items = Wishlist.objects.filter(user=request.user)
	return render(request, 'wishlist/wishlist.html', {'items':items})



@login_required
def add_to_wishlist(request, product_id):
	item = get_object_or_404(Product, id=product_id)
	item_name = item.name

    # product = Product.objects.get(id=product_id
    # slug = item.slug
    # wished_item,created = Wishlist.objects.get_or_create(wished_item=item, user = request.user)
	wished_item = Wishlist.objects.create(wished_item=item, user = request.user, name=item_name)
	# wished_item.quantity += 1
	wished_item.save()

    # wished_item,created.save()
    # return redirect('shop:ProdCatDetail', slug=product_id)
	return redirect('shop:allProdCat')

@login_required
def delete_item_wishlist(request, product_id):
	item = get_object_or_404(Product, id=product_id)
	item_name = item.name
	wished_item = Wishlist.objects.get(wished_item=item, user = request.user, name=item_name)
	# wished_item.quantity -= 1
	wished_item.delete()
    # product = Product.objects.get(id=product_id
    # slug = item.slug
    # wished_item,created = Wishlist.objects.get_or_create(wished_item=item, user = request.user)
    # wished_item = Wishlist.objects.delete(wished_item=item, user = request.user)
    # wished_item.save()
    # print(wished_item)
    # wished_item,created.save()
    # return redirect('shop:ProdCatDetail', slug=product_id)
	return redirect('shop:allProdCat')
