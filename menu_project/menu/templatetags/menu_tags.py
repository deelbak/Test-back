from django import template
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_title):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.get(title=menu_title)
        menu_items = menu.items.all()
    except Menu.DoesNotExist:
        menu = None
        menu_items = []

    active_item = None
    for item in menu_items:
        if item.get_absolute_url() == current_path:
            active_item = item
            break

    def get_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = get_menu_tree(items, item)
                tree.append((item, children))
        return tree

    menu_tree = get_menu_tree(menu_items)
    return {'menu_tree': menu_tree, 'active_item': active_item, 'current_path': current_path}
