from django import template

register = template.Library()

@register.filter
def percentage(discounted_price, original_price):
    if original_price:
        return round((1 - (discounted_price / original_price)) * 100)
    return 0
