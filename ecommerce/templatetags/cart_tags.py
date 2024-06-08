from django import template
from courses.models import CartItem

register = template.Library()

@register.inclusion_tag('base.html', takes_context=True)
def show_cart(context):
    request = context['request']
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.total_price for item in cart_items)
        return {'cart_items': cart_items, 'total_price': total_price}
    else:
        return {'cart_items': [], 'total_price': 0}
