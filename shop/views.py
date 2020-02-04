from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product, ProductImages
from wishlist.models import Wishlist
from blog.models import Blog
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm, ProductSizeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# def wishlist(request):
# 	return render(request, 'wishlist.html', {})
#
#
#
# @login_required
# def add_to_wishlist(request, product_id):
# 	item = get_object_or_404(Product, id=product_id)
# 	# product = Product.objects.get(id=product_id)
# 	wished_item,created = Wishlist.objects.get_or_create(wished_item=item, user = request.user)
# 	return redirect('index.html')


def index(request):
	text_var = 'This is my first django app web page.'
	products = Product.objects.all().order_by('-created')
	popularproducts = Product.objects.all().order_by('views')
	blogs = Blog.objects.all().order_by('-created')
	return render(request, 'index.html', {'products': products, 'popularproducts': popularproducts, 'blogs': blogs })

def about(request):
	return render(request, 'about.html', {})


#Category view

def allProdCat(request, c_slug=None):
	c_page = None
	products_list = None
	if c_slug != None:
		c_page = get_object_or_404(Category,slug=c_slug)
		products_list = Product.objects.filter(category=c_page,available=True)
	else:
		products_list = Product.objects.all().filter(available=True)
	'''Pagination code'''
	paginator= Paginator(products_list, 6)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
	try:
		products = paginator.page(page)
	except (EmptyPage,InvalidPage):
		products = paginator.page(paginator.num_pages)
	return render(request, 'shop/category.html',{'category':c_page, 'products':products})

def ProdCatDetail(request,c_slug,product_slug):
	try:
		product = Product.objects.get(category__slug=c_slug,slug=product_slug)
		psize = ProductSizeForm(request.GET)
		product_images = ProductImages.objects.filter(productpictures = product)
		product.views +=1
		item_name = product.name
		user = request.user
		if not request.user.is_authenticated:
			wishlist = []
		else:
			try:
				wishlist = Wishlist.objects.get(wished_item=product, user = request.user, name=item_name)
			except Wishlist.DoesNotExist:
				wishlist = None
		# if user.is_authenticated:
		# 	try:
		# 		wishlist = Wishlist.objects.get(wished_item=product, user = request.user, name=item_name)
		# 	except Wishlist.DoesNotExist:
		# 		wishlist = None
		# wishlist = Wishlist.objects.filter(user=request.user)
		# if wishlist == 0:
		# 	wishlist = Wishlist.objects.filter(wished_item=product, user = request.user, name=item_name)
		# else:
		# 	wishlist = Wishlist.objects.get(wished_item=product, user = request.user, name=item_name)
		# else:
		# 	pass

	except Exception as e:
		raise e
	return render(request,'shop/product.html', {'product':product, 'psize': psize, 'wishlist': wishlist, 'product_images': product_images})

def signupView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			signup_user = User.objects.get(username=username)
			customer_group = Group.objects.get(name='Customer')
			customer_group.user_set.add(signup_user)
			password = form.cleaned_data.get('password1')
			# once the user is created it will do an auhtenticate or better said a login by taking the username and the password variables 
			user = authenticate(username=username, password=password)
			login(request, user)
	else:
		form = SignUpForm()
	return render(request, 'accounts/signup.html', {'form':form})

def signinView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('shop:allProdCat')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/signin.html', {'form':form})

def signoutView(request):
	logout(request)
	return redirect('signin')
