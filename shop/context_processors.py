from .models import Category
def menu_links(request):
        links = Category.objects.all()
        return dict(links=links)

# def get_items_in_wishlist_count(request):
#     wishlist = request.session.get('wishlist', {})
#     count = 0
#     for id,quantity in wishlist.items():
#         count+=quantity
#
#     return {'items_in_wishlist':count}
