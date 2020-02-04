from wishlist.models import Wishlist

def wishes(request):
    wishcount = 0
    user = request.user
    if 'admin' in request.path:
        return {}

    elif not request.user.is_authenticated:
        pass
    else:
        try:
            wishes = Wishlist.objects.all().filter(user = user)
            for wish in wishes:
                wishcount = wishcount + 1
        except Wishlist.DoesNotExist:
            wishcount = 0
    return dict(wishcount = wishcount)
