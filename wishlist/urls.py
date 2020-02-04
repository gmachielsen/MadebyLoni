from django.urls import path
from . import views

app_name='wishlist'

urlpatterns = [

	path('wishlist', views.wishlist, name='wishlist'),
    path('added_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
	path('delete_item_wishlist<int:product_id>/', views.delete_item_wishlist, name='delete_item_wishlist')
]
