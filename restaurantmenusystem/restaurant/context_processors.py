from restaurant.models import Menu
def links(request):
    c=Menu.objects.all()
    return {'links':c}