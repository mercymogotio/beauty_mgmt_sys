from django import template

register = template.Library()

@register.filter
def average_rating(ratings):
    if not ratings:
        return 0  # Return 0 if there are no ratings
    total = sum([rating.rating for rating in ratings])
    return total / len(ratings)
